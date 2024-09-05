import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
import os
from dotenv import load_dotenv
from loguru import logger

logger.info("punto de control interno 1")

# Cargamos variables de entorno desde el archivo .env
load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]
chroma_client = chromadb.Client()

df = pd.read_csv("./app/data/movies_dataset_oficial.csv")

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
    for adult, release_date in zip(df["adult"].tolist(), df["release_date"].tolist()):
        metadata = {"adult": adult, "release_date": release_date}
        metadatas.append(metadata)

    return ids, documents, metadatas


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


def initialize_chroma_client():
    """
    Inicializa el cliente ChromaDB y crea la colección.

    Returns:
        collection: Colección ChromaDB.
    """

    collection = chroma_client.create_collection(
        name="movies_collection",
        embedding_function=embedding_functions.OpenAIEmbeddingFunction(
            api_key=api_key, model_name="text-embedding-3-small"
        ),
    )
    return collection

    # Cargamos la data


ids, documents, metadatas = load_data(df)

# Inicializamos el cliente de Chroma y creamos la coleccion
collection = initialize_chroma_client()

# Ahora definimos el tamaño de los lotes
batch_size = 100
total_items = len(ids)
num_batches = (total_items + batch_size - 1) // batch_size

logger.info("punto de control interno 3")


# Insertamos los lotes con la data a la collection
for batch_index in range(num_batches):
    logger.info(f"Insertando lote {batch_index + 1}/{num_batches}")
    start_index, end_index = calculate_indices(batch_index, batch_size, total_items)
    response = collection.add(
        ids=ids[start_index:end_index],
        documents=documents[start_index:end_index],
        metadatas=metadatas[start_index:end_index],
    )

logger.info("punto de control interno 4")