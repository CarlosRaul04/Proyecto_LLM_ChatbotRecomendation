import pandas as pd
import os

def readcsv(ruta_dataset, genres: list[str] = ["action", "fiction"]):

    if not os.path.exists(ruta_dataset):
        raise FileNotFoundError(f"No se encontró el archivo en la ruta: {ruta_dataset}")

    #Leemos la ruta
    df = pd.read_csv(path)

    #Convertimos los generos a minúsculas
    df['genres'] = df['genres'].str.lower()

    #Definimos filtered_Df
    filtered_df = df

    #Filtramos
    for genre in genres:
        filtered_df = filtered_df[
            filtered_df['genres'].str.contains(genre)
        ]

    #Seleccionamos solo 1000 registros
    if len(filtered_df) >= 1000:
        df_1000 = filtered_df.sample(n=1000)
    else: 
        df_1000 =filtered_df
        
    return df_1000


def data_generation(df, ruta_salida):

    #Validamos que el df no esté vacio
    if df.empty:
        raise ValueError("El DataFrame está vacío. No se puede generar la salida.")

    #Creamos la nueva columna con la data que le pasaremos a la base de datos vectorial
    df['data'] = df.apply(
        lambda row: f"Titulo: {row['title']}, Estado: {row['status']}, Sinopsis: {row['overview']}, "
                f"Generos: {row['genres']}, Empresas_productoras: {row['production_companies']}, "
                f"Idiomas_hablados: {row['spoken_languages']}, palabras_clave: {row['keywords']}",
        axis=1
    )   

    #Validamos que la ruta de salida es válida
    output_dir = os.path.dirname(ruta_salida)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #Ponemos la ruta a la que queremos cargar el nuevo archivo csv
    df.to_csv(ruta_salida, index=False)


if __name__ == '__main__':

    #Ponemos la ruta
    path = "D:\Cursos\Curso-BOOTCAMP-IA-GENERATIVA-SOLUCIONES-CON-PYTHON\TMDB_movie_dataset_v11.csv"
    #Ruta de salida
    ruta_salida = 'D:\Cursos\Curso-BOOTCAMP-IA-GENERATIVA-SOLUCIONES-CON-PYTHON/movies_dataset_oficial.csv'

    #Procesamos el dataset
    df_filtrado = readcsv(path)

    #Generamos el nuevo dataset
    data_generation(df_filtrado, ruta_salida)

