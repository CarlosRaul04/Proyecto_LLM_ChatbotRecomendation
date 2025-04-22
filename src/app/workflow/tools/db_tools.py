from langchain_core.tools import tool
from app.data.db.queries import get_oscar_by_actor, get_oscarWinners_Or_Losers_by_year, get_oscar_by_movie, get_categories, get_oscars_by_categoy_and_year


@tool
def search_oscars_by_actor(name: str):
    """Use this tool to find the Oscars for which the actor has been nominated"""
    
    try:
        if not isinstance(name, str) or not name.strip():
            return {"error": "El nombre del actor debe ser una cadena no vacía."}

        awards = get_oscar_by_actor(name)

        if not awards:
            return {"message": "No se encontraron premios Oscar para el actor especificado."}

        return {"awards": awards}

    except Exception as e:
        return {"error": f"Se produjo un error inesperado: {e}"}
    


@tool
def search_oscarWinners_Or_Losers_by_year(year: int, winner: bool):
    """
    Use this tool to find Oscar winners or losers based on the specified year.

    Arguments:
    year (int): The year of the Oscars that you want to consult. It must be a non-empty integer.
    winner (bool): Specifies whether to obtain the winners or losers. Use True for winners and False for losers.
    
    Returns:
    dict: A dict with the Oscar results or an error message if no data is found.
    """
    
    try:
        if not isinstance(year, int) or year == "":
            raise ValueError("El año debe ser un entero no vacío.")
        
        if not isinstance(winner, bool) or bool == "":
            raise ValueError("El winner debe ser true o false.")
        
        awards = get_oscarWinners_Or_Losers_by_year(year, winner)

        if not awards:
            return {"message": "No se encontraron premios Oscar para el año especificado."}

        return {"awards": awards}

    except Exception as e:
        return {"error": f"Se produjo un error inesperado: {e}"}
    


@tool
def search_oscars_by_movie(movie: str):
    """Use this tool to find the Oscars or categories the film has been nominated for."""
    
    try:
        if not isinstance(movie, str) or not movie.strip():
            return {"error": "El nombre de la película debe ser una cadena no vacía."}

        awards = get_oscar_by_movie(movie)

        if not awards:
            return {"message": "No se encontraron nominaciones a los Oscar para la película especificada."}

        return {"awards": awards}

    except Exception as e:
        return {"error": f"Se produjo un error inesperado: {e}"}
    

@tool
def search_categories():
    """use this tool to find the oscar categories"""
    
    try:
        
        categories = get_categories()

        if not categories:
            return {"message": "No se encontraron categorias"}

        return {"categories": categories}

    except Exception as e:
        return {"error": f"Se produjo un error inesperado: {e}"}
    


@tool
def search_oscars_by_categoy_and_year(year: int, category: str):
    """
    Use this tool to find the films and actors nominated for the Oscar according to the year and category.

    Arguments:
    year (int): The year of the Oscars you want to consult. It must be a non-empty integer. By default it is 2024
    category (string): Specifies the category of the award. Receive the category delivered by the user (translate it into English).
    
    Returns:
    dict: A dict with the movies and actors results or an error message if no data is found.
    """
    
    try:
        if not isinstance(year, int) or not category.strip():
            raise ValueError("El año debe ser un entero no vacío.")
        
        if not isinstance(category, str) or bool == "":
            raise ValueError("La categoría debe ser una cadena no vacia.")
        
        awards = get_oscars_by_categoy_and_year(year, category)

        if not awards:
            return {"message": "No se encontraron películas o actores para la categoría especificada."}

        return {"awards": awards}

    except Exception as e:
        return {"error": f"Se produjo un error inesperado: {e}"}
    