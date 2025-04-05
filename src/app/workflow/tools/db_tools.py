from langchain_core.tools import tool
from app.data.db.queries import get_oscar_by_actor


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