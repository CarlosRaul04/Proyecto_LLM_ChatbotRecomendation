import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY_TMDB = os.getenv('API_KEY_TMDB')
account = os.getenv('account')
BASE_URL_TMBD_V4 = f"https://api.themoviedb.org/4/"


def get_headers():
    """Genera los encabezados necesarios para la petición a la API"""
    return {
        "accept": "application/json",
        'Authorization': f'Bearer {API_KEY_TMDB}'
    }



def handle_response(response):
    """Maneja la respuesta de la API, devolviendo un JSON si es exitosa o un error si falla"""

    if response.status_code == 200:
        return response.json()
    else:
        return {'Error': f"{response.status_code}: {response.reason}"}


#Funcion para buscar películas recomendadas por la api 
def recommendedMovies(page: int):
    """Obtiene recomendaciones de películas"""
    endpoint = f'account/{account}/movie/recommendations'
    url = f"{BASE_URL_TMBD_V4}{endpoint}"

    # Parámetros
    params = {
        'page': page,
        'language': 'en-US'
    }  

    try:
        response = requests.get(url, headers=get_headers(), params=params)
        return handle_response(response)
    except requests.exceptions.RequestException as e:
        return {'Error': f"Request failed: {e}"}
    

#Función para buscar series recomendadas por la api
def recommendedTVShows(page: int):
    """Obtiene recomendaciones de películas"""
    endpoint = f'account/{account}/tv/recommendations'
    url = f"{BASE_URL_TMBD_V4}{endpoint}"

    # Parámetros
    params = {
        'page': page,
        'language': 'en-US'
    }  

    try:
        response = requests.get(url, headers=get_headers(), params=params)
        return handle_response(response)
    except requests.exceptions.RequestException as e:
        return {'Error': f"Request failed: {e}"}
    