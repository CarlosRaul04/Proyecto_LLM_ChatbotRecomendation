import uuid
import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from loguru import logger
from app import MovieAgent
logger.info("punto de control 1")
from app.cache.mycache import collection
logger.info("punto de control 2")

# Configuración básica de la página
st.set_page_config(page_title="MovieChat", layout="centered")

st.title("MovieChat")


# Inicializamos el chat
if "messages" not in st.session_state:
    st.session_state.messages = []

if "movie_agent" not in st.session_state:
    # Inicializa tu agente MovieAgent aquí
        st.session_state["movie_agent"] = MovieAgent
        logger.info("Agente inicializado correctamente.")

# Función para verificar si la pregunta ya está en el caché
def check_cache(question):
    """Check cache for an answer"""
    cache_result = collection.query(
        query_texts=[question],
        n_results=1
    )

    no_result = len(cache_result["documents"][0]) == 0

    if no_result:
        logger.info('No hit in cache')
        return None

    distance = cache_result["distances"][0][0]
    distant_results = distance > 0.3
    if distant_results:
        logger.info(f'Cache results distant: [{distance}]')
        return None

    answer = cache_result["metadatas"][0][0]['answer']
    logger.info(f'Cache hit: [{distance}] {answer[:30]}...')
    return answer + '\n\n`cached`'  # Añadimos "cached" si la respuesta es del caché

# Función para almacenar la respuesta en el caché
def write_answer_to_cache(question, answer):
    random_id = str(uuid.uuid4())[:8]
    collection.add(
        documents=[question],
        ids=[random_id],
        metadatas=[{"answer": answer}]
    )

# Función para obtener la respuesta del agente (o desde el caché si existe)
def get_response():
    try:
        # Tomar el último mensaje del usuario
        question = st.session_state["messages"][-1]["content"]

        # Intentar obtener la respuesta desde el caché
        cached_answer = check_cache(question)
        if cached_answer:
            logger.info("Respuesta obtenida del caché.")

            st.markdown(cached_answer)

            # Agregar la respuesta al historial de mensajes

            return cached_answer  # Si es del caché, retornamos la respuesta directamente
        else:

            message_placeholder = st.empty()
            with message_placeholder:
                st.markdown("Buscando...") 
            full_response = ""

    

    
            for response_chunk in st.session_state["movie_agent"].stream(
                    input={"messages": st.session_state["messages"][-1]["content"]},  
                    config={"configurable": {"thread_id": 0}}
                ):
                # Obtener los mensajes devueltos por el agente
                messages = response_chunk.get("agent", {}).get("messages", [])
                for message in messages:
                    full_response += message.content
                    message_placeholder.markdown(full_response + "▌")

            # Eliminamos el cursor cuando la respuesta esté completa
            full_response += '\n\n`gpt`'  # Añadimos "gpt" al final si es del agente
            message_placeholder.markdown(full_response)

            # Guardar la respuesta en el caché
            write_answer_to_cache(question, full_response)
            
            return full_response

    except Exception as e:
        logger.error(f"Error durante la generación de la respuesta: {str(e)}")
        st.error("Hubo un problema generando la respuesta del agente.")

# Mostrar mensajes de chat del historial al volver a ejecutar la aplicación
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Manejo de la entrada del usuario
if prompt := st.chat_input("¿Qué piensas?"):
    try:
        # Agregar el mensaje del usuario al historial completo
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Mostrar el mensaje del usuario en el chat
        with st.chat_message("user"):
            st.markdown(prompt)

        # Llamamos a la función para generar la respuesta del agente (o del caché)
        with st.chat_message("assistant", avatar="👽"):
            full_response = get_response()

            st.session_state.messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        logger.error(f"Error al procesar la entrada del usuario: {str(e)}")
        st.error("Hubo un problema procesando tu mensaje.")

logger.info("Se insertaron correctamente los mensajes.")
