import json
from langchain_core.tools import tool
from app.services.tmdb_api import top_rated_TV
from app.services.tmdb_apiV4 import recommendedTVShows


@tool
def TvTopRated(page: int):
    """use this tool to get the best rated series in history with their small sipnopsis. 
    They will be in decreasing order
    
    Arguments:
    page -- the page of results to fetch (pagination)

    """
    #Validación de entrada
    if not isinstance(page, int) or page <= 0:
        return "Error: El número de página debe ser un entero positivo."

    try:
        #Llamada a la función que obtiene datos de la api
        tv_shows = top_rated_TV(page)

        if not tv_shows or 'results' not in tv_shows:
            return "No ha sido posible encontrar las series"

        #Procesar los datos para mostrar la información que yo quiera
        formatted_shows = []
        for show in tv_shows['results']:
            formatted_shows.append({
                'id': show.get('id', 'id no disponible'),
                'title': show.get('name', 'Título desconocido'),
                'genre_ids': show.get('genre_ids', 'Géneros no disponibles'),
                'overview': show.get('overview', 'Sinopsis no disponible'),
                'vote_average': show.get('vote_average', 'rate no disponible'),
                'vote_count': show.get('vote_count', 'vote count no disponible'),
                'release_date': show.get('release_date', 'año de lanzamiento no disponible'),
                'poster_path': show.get('poster_path', 'foto no disponible'),

            })

        #Crear la estructura del JSON de respuesta
        response_data = {
            "page": page,
            "total_results": tv_shows.get('total_results', 0),
            "total_pages": tv_shows.get('total_pages', 0),
            "shows": formatted_shows
        }


        response_format = json.dumps(response_data, indent=4)

        return f"## TV SHOWS Top Rated (Page {page}):\n{response_format}"

    except Exception as e:
        #Manejo de errores para problemas inesperados
        return f"Error al obtener las series: {str(e)}"
    


@tool
def apiTVShowsRecommendations(page: int):
    """Use this tool when the user asks for non-personalized recommendations, 
    when he/she only wants you to recommend or list good movies."""

    apiTVShows = recommendedTVShows(page)

    if not apiTVShows:
        return f"Lo siento no tengo recomendaciones rápidas ahora mismo " 
    
    TVShowsContent = json.dumps(apiTVShows)

    formated_response = f"## Recommended TV Shows: {TVShowsContent}"
    
    return formated_response
