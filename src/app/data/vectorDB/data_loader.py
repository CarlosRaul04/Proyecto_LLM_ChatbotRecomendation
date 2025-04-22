import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
import os
from dotenv import load_dotenv
from loguru import logger
from concurrent.futures import ThreadPoolExecutor

logger.info("punto de control interno 1")

# Cargamos variables de entorno desde el archivo .env
load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]
chroma_client = chromadb.Client()

df = pd.read_csv("./app/datasets/movies_dataset_oficial.csv")

logger.info("punto de control interno 2")


def load_data(df):
    """
    Convierte el DataFrame en listas de IDs, documentos y metadatos.

    Args:
        df (pd.DataFrame): El DataFrame que contiene las columnas 'id', 'data' y las demas que quieras ingresar como metadatas.

    Returns:
        tuple: Contiene tres listas: ids, documents, y metadatas.
    """

    ids = df["id"].astype(str).tolist()
    documents = df["data"].tolist()
    metadatas = []

    # Elejimos que metadata ingresaremos
    for adult, release_date, vote_average in zip(df['adult'].tolist(), df['release_date'].tolist(), df['vote_average'].tolist()):
        metadata = {
            'adult': adult,
            'release_date': release_date,
            'vote_average': vote_average
        }
        metadatas.append(metadata)

    return ids, documents, metadatas



def initialize_chroma_client():
    """
    Inicializa el cliente ChromaDB y crea la colección.

    Returns:
        collection: Colección ChromaDB.
    """

    return chroma_client.create_collection(
        name="movies",
        embedding_function=embedding_functions.OpenAIEmbeddingFunction(
            api_key=api_key, model_name="text-embedding-3-small"
        ),
    )



def calculate_indices(batch_index, batch_size, total_items):
    """
    Calcula los índices de inicio y fin para un lote de datos.

    Args:
        batch_index (int): Índice del lote actual.
        batch_size (int): Tamaño del lote.
        total_items (int): Número total de elementos.

    Returns:
        tuple: Índices de inicio y fin para el lote.

    """

    start_index = batch_index * batch_size
    end_index = min((batch_index + 1) * batch_size, total_items)
    return start_index, end_index



# Función para insertar lote
def insert_batch(collection, batch_index, ids, documents, metadatas, batch_size, total_items):
    start_index, end_index = calculate_indices(batch_index, batch_size, total_items)
    collection.add(
        documents=documents[start_index:end_index],
        ids=ids[start_index:end_index],
        metadatas=metadatas[start_index:end_index],
    )
    logger.info(f"Insertado lote {batch_index + 1}")



#Cargamos la data

ids, documents, metadatas = load_data(df)
collection = initialize_chroma_client()

batch_size = 1000
total_items = len(ids)
num_batches = (total_items + batch_size - 1) // batch_size

# Inserción paralelizada de los lotes
with ThreadPoolExecutor(max_workers=4) as executor:
    for batch_index in range(num_batches):
        executor.submit(insert_batch, collection, batch_index, ids, documents, metadatas, batch_size, total_items)

    logger.info("Proceso completado")