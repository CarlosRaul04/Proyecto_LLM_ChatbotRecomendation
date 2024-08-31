from langchain_core.tools import tool
from langchain.schema import SystemMessage, HumanMessage
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import json

load_dotenv()

#Llamamos al modelo
gpt_4o_mini = ChatOpenAI(model="gpt-4o-mini", temperature=0)


WRITER_SYSTEM_MOVIE= """
You will receive the API request data with the title of the searched movie as "title" and the API response content as "content". Your task is to:

1. Create a friendly synopsis that describes what the movie is about based on the information provided.
  
2. Extract and return only the relevant information for movies whose title exactly matches the "title" provided by the user. If the content includes movies unrelated to the requested title, ignore them.

3. If you detect a possible spelling error in the title, notify the user and suggest the correct title based on your understanding.

4. If the title is correct, provide the essential information about the matching movie(s) found within the API content. If the movie is part of a franchise and there are multiple related movies, include them as well.

Make sure the friendly synopsis is informative and engaging, but do not invent or add any movies that are not present in the content provided.
"""

@tool
def search_title(title: str):
    """Use this tool when the user requests detailed information about a specific movie. 
    The tool searches for movies with the exact title provided by the user and returns movies containing that title and
    relevant information. If the title is misspelled, it suggests a correction. 
    """
    
    #Esta variable almacenará las películas encontradas con el title
    movies = search_movie(title)

    #Validamos
    if not movies:
        return f"Lo siento, no encontramos películas con ese título '{title}'"
    
    #Mejoramos el formato
    movies_content = json.dumps(movies)

    #mandamos el contenido a un modelo gpt para que lo filtre
    try:
        response = gpt_4o_mini.invoke(
            input=[
                SystemMessage(content=WRITER_SYSTEM_MOVIE),
                HumanMessage(content=f"Title: {title}, content: {movies_content}")

            ]
        ).content
    except Exception as e:
        return f"Ha ocurrido un error procesando tu petición: {str(e)}"
    

    formated_response = f"## Movie Information: {title}\n\n{response}"

    return formated_response

    


    

@tool
def recommendation(texts: list[str], num_results: int = 3):
    """
    Use this tool to provide movie recommendations based on the user's tastes and the information they provide.
    
    Parameters:
    - texts: A list of strings containing the user's input or preferences.
    - num_results: The number of movie recommendations to return (default is 3), you must put the number of results the user requests.
    
    Returns:
    - A dictionary containing the recommended movies along with relevant details such as title, description, and other metadata.
    """
    
    #Validamos la entrada
    if not isinstance(texts, list) or not all (isinstance(text, str) for text in texts):
        return {"error": "la entrada debe de ser una lista de cadenas."}
    
    if not isinstance(num_results, int) or num_results <= 0:
        return{"error": "num_results debe de ser un int positivo"}
    
    results = collection.query(
        query_texts=texts,
        n_results=num_results
    )   

    #Validamos el número de resultados
    if not results or len(results['documents']) < num_results:
        return {"message": "No se encontraron suficientes resultados. Aquí tienes las recomendaciones disponibles."}

    #Enriquecemos el resultado

    enriched_results = []
    for i in range(num_results): 
        enriched_results.append({
            "id": results['ids'][i],
            "data_movie": results['documents'][i],
            "metadatas": results['metadatas'][i]

        })

    return enriched_results
