import pandas as pd
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv
import os

#Cargamos variables de entorno desde el archivo .env
load_dotenv()

df = pd.read_csv('D:\Cursos\Curso-BOOTCAMP-IA-GENERATIVA-SOLUCIONES-CON-PYTHON/movies_dataset_oficial.csv')

def load_data(df):
    """
    Convierte el DataFrame en listas de IDs, documentos y metadatos.

    Args:
        df (pd.DataFrame): El DataFrame que contiene las columnas 'id', 'data' y las demas que quieras ingresar como metadatas.

    Returns:
        tuple: Contiene tres listas: ids, documents, y metadatas.
    """

    ids = df['id'].astype(str).tolist()
    documents = df['data'].tolist()
    metadatas = []

    #Elejimos que metadata ingresaremos
    for adult, release_date in zip(df['adult'].tolist(), df['release_date'].tolist()):
        metadata = {
            'adult': adult,
            'release_date': release_date
        }
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
    api_key = os.getenv('API_KEY') #Cargamos la API KEY DESDE .env
    chroma_client = chromadb.Client()
    collection= chroma_client.create_collection(
        name="movies_collection",
        embedding_function=embedding_functions.OpenAIEmbeddingsFunction(
            api_key=api_key,
            model_name="text-embedding-3-small"
        )
    )
    return collection


if __name__ == "__main__":

    df = pd.read_csv('D:\Cursos\Curso-BOOTCAMP-IA-GENERATIVA-SOLUCIONES-CON-PYTHON/movies_dataset_oficial.csv')
    #Cargamos la data
    ids, documents, metadatas = load_data(df)

    #Inicializamos el cliente de Chroma y creamos la coleccion
    collection = initialize_chroma_client()

    #Ahora definimos el tamaño de los lotes
    batch_size = 100
    total_items = len(ids)
    num_batches = (total_items + batch_size - 1) // batch_size

    #Insertamos los lotes con la data a la collection
    for batch_index in range(num_batches):
        start_index, end_index = calculate_indices(batch_index, batch_size, total_items) 
        response = collection.add(
            ids= ids[start_index:end_index],
            documents=documents[start_index:end_index],
            metadatas=metadatas[start_index:end_index]
        )

