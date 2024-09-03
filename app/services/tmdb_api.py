import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY_TMDB = os.getenv('API_KEY_TMDB')
URL_TMBD = 'https://api.themoviedb.org/3/search/movie'


#Funcion para buscar películas por título
def search_movie(title: str):
    # Parámetros
    params = {
        'query': title,
        'language': 'en-US',
        'page': 1
    }  

    #Colocamos el código de autorización
    headers = {
        'Authorization': f'Bearer {API_KEI_TMDB}',
        'accept': 'application/json'
    }

    response = requests.get(URL_TMBD, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {'Error': f"{response.status_code}"}