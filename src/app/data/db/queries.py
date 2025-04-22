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
    



def get_oscarWinners_Or_Losers_by_year(year: int, winner: bool):
    """Esta función devuelve los ganadores o perdedores de los oscar segun el año"""

    # Validación de parámetros
    if not isinstance(year, int) or year == "":
        return ValueError("El año debe ser un entero no vacío.")

    # Obtener la sesión
    try:
        db = next(get_db())
    except StopIteration:
        raise RuntimeError("No se pudo obtener una sesión de base de datos.")

    try:
        # Realizamos la consulta
        result = db.execute(
            text("SELECT * FROM oscar_awards WHERE year_ceremony = :year AND winner = :winner"),
            {'year': year, 'winner': winner}
        ).fetchall()

        if not result: 
            return {"message": "No se encontraron premios Oscar para el año especificado."}

        return result

    except SQLAlchemyError as e:
        #Manejo de errores específicos de SQLAlchemy
        print(f"Error al ejecutar la consulta: {e}")
        return {"error": "Error en la consulta a la base de datos"}
    except Exception as e:
        #Manejo de errores generales
        print(f"Se produjo un error inesperado: {e}")
        return {"error": "Se produjo un error inesperado"}




def get_categories():
    """Esta función obtiene las categorias de los oscar"""

    # Obtener la sesión
    try:
        db = next(get_db())
    except StopIteration:
        raise RuntimeError("No se pudo obtener una sesión de base de datos.") 

    try:

        #Realizamos la consulta
        result = db.execute(
            text("SELECT DISTINCT category FROM oscar_awards where year_ceremony = 2024")
        ).fetchall()

        if not result: 
            return {"message": "No se encontraron categorias"}
        
        return result

    except SQLAlchemyError as e:
        #Manejo de errores específicos de SQLAlchemy
        print(f"Error al ejecutar la consulta: {e}")
        return {"error": "Error en la consulta a la base de datos"}
    except Exception as e:
        #Manejo de errores generales
        print(f"Se produjo un error inesperado: {e}")
        return {"error": "Se produjo un error inesperado"}
    


def get_oscar_by_movie(movie: str):
    """Esta función obtiene las nominaciones a los oscars de una película"""

    # Validación de parámetros
    if not isinstance(movie, str) or not movie.strip():
        raise ValueError("El nombre de la película debe ser una cadena no vacía.")

    # Obtener la sesión
    try:
        db = next(get_db())
    except StopIteration:
        raise RuntimeError("No se pudo obtener una sesión de base de datos.") 

    try:

        #Realizamos la consulta
        query = f"%{movie}%"
        result = db.execute(
            text("SELECT * FROM oscar_awards WHERE film ILIKE :movie"),
            {'movie': query}
        ).fetchall()

        if not result: 
            return {"message": "No se encontraron nominaciones a los oscar para la película especificada"}
        
        return result

    except SQLAlchemyError as e:
        #Manejo de errores específicos de SQLAlchemy
        print(f"Error al ejecutar la consulta: {e}")
        return {"error": "Error en la consulta a la base de datos"}
    except Exception as e:
        #Manejo de errores generales
        print(f"Se produjo un error inesperado: {e}")
        return {"error": "Se produjo un error inesperado"}
    

def get_oscars_by_categoy_and_year(year: int, category: str):
    """Esta función devuelve las películas y actores nominados al oscar segun el año y categoria"""

    # Validación de parámetros
    if not isinstance(year, int) or year == "":
        return ValueError("El año debe ser un entero no vacío.")

    if not isinstance(category, str) or not category.strip():
        raise ValueError("La categoria debe ser una cadena no vacía.")

    # Obtener la sesión
    try:
        db = next(get_db())
    except StopIteration:
        raise RuntimeError("No se pudo obtener una sesión de base de datos.")

    try:
        # Realizamos la consulta
        query = f"%{category}%"
        result = db.execute(
            text("SELECT year_film, category, actor_name, film, winner FROM oscar_awards WHERE category ILIKE :category AND year_ceremony = :year"),
            {'year': year, 'category': query}
        ).fetchall()

        if not result: 
            return {"message": "No se encontraron premios Oscar para el año especificado."}

        return result

    except SQLAlchemyError as e:
        #Manejo de errores específicos de SQLAlchemy
        print(f"Error al ejecutar la consulta: {e}")
        return {"error": "Error en la consulta a la base de datos"}
    except Exception as e:
        #Manejo de errores generales
        print(f"Se produjo un error inesperado: {e}")
        return {"error": "Se produjo un error inesperado"}