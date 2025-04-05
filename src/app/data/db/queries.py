from app.data.db.connection import get_db
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

def get_oscar_by_actor(name: str):
    """Esta función obtiene los oscars a los que ha sido nominado el actor"""

    # Validación de parámetros
    if not isinstance(name, str) or not name.strip():
        raise ValueError("El nombre del actor debe ser una cadena no vacía.")

    # Obtener la sesión
    try:
        db = next(get_db())
    except StopIteration:
        raise RuntimeError("No se pudo obtener una sesión de base de datos.") 

    try:

        #Realizamos la consulta
        query = f"%{name}%"
        result = db.execute(
            text("SELECT * FROM oscar_awards WHERE actor_name ILIKE :name"),
            {'name': query}
        ).fetchall()

        if not result: 
            return {"message": "No se encontraron premios oscar para el actor especificado"}
        
        return result

    except SQLAlchemyError as e:
        #Manejo de errores específicos de SQLAlchemy
        print(f"Error al ejecutar la consulta: {e}")
        return {"error": "Error en la consulta a la base de datos"}
    except Exception as e:
        #Manejo de errores generales
        print(f"Se produjo un error inesperado: {e}")
        return {"error": "Se produjo un error inesperado"}
    