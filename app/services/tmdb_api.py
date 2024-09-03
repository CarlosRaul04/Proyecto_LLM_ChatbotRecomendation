import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY_TMDB = os.getenv('API_KEY_TMDB')
BASE_URL_TMBD = 'https://api.themoviedb.org/3/'


def get_headers():
    """Genera los encabezados necesarios para la petición a la API"""
    return {
        "accept": "application/json",
        'Authorization': f'Bearer {API_KEY_TMDB}',
    }


def handle_response(response):
    """Maneja la respuesta de la API, devolviendo un JSON si es exitosa o un error si falla"""

    if response.status_code == 200:
        return response.json()
    else:
        return {'Error': f"{response.status_code}: {response.reason}"}


#PETICIONES 

#Funcion para buscar películas por título
def search_movie(title: str):
    """Busca películas por título usando la API de TMDB"""

    endpoint = 'search/movie'
    url = f"{BASE_URL_TMBD}{endpoint}"

    # Parámetros
    params = {
        'query': title,
        'language': 'en-US',
        'page': 1
    }  


    try:
        response = requests.get(url, headers=get_headers(), params=params)
        return handle_response(response)
    except requests.exceptions.RequestException as e:
        return {'Error': f"Request failed: {e}"}
    
    
