import streamlit as st
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from loguru import logger

logger.info("punto de control 1")
from app import MovieAgent

logger.info("punto de control 2")

# Configuración básica de la página
st.set_page_config(page_title="MovieChat", layout="centered")

st.title("MovieChat")
# Ejemplo de input del usuario

#Inicializamos el chat
if "messages" not in st.session_state:
    st.session_state.messages = []

if "movie_agent" not in st.session_state:
    # Inicializa tu agente MovieAgent aquí
    st.session_state["movie_agent"] = MovieAgent

#Mostrar mensajes de chat del historial al volver a ejecutar la aplicación
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Función del agente
def get_response():
    message_placeholder = st.empty()
    message_placeholder.markdown("Buscando...") # Muestra "Buscando..." mientras se obtiene la respuesta
    full_response = ""

    #Llama al método stream de MovieAgent
    for response_chunk in st.session_state["movie_agent"].stream(
            input={"messages": st.session_state["messages"]},
            config={
                "configurable": {
                    "thread_id": 0
                }
            }
        ):
            

            messages = response_chunk.get("agent", {}).get("messages", [])
            for message in messages:
                full_response += message.content
                message_placeholder.markdown(full_response + "▌")

    # Eliminamos el cursor cuando la respuesta esté completa

    message_placeholder.markdown(full_response)
    st.session_state["messages"].append({"role": "assistant", "content": full_response})
        
    


if prompt := st.chat_input("¿Que piensas?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    #LLamamos a la función para generar la respuesta del agente
    with st.chat_message("assistant", avatar="👽"):
        get_response()

       
    
logger.info("Se insertó de manera correcta los mensajes")


#user_input = st.text_input("MovieChat")
#print("antes del if")
#logger.info("punto de control 3")
#if user_input:
 #   print("dentro del if")
    # Aquí va la lógica de recomendación de películas usando el chatbot
    # Por simplicidad, solo mostraremos el input del usuario
  #  st.write(f"Buscando películas que coincidan con: {user_input}")
    # Aquí puedes llamar a tu función de recomendación y mostrar resultados

    # Usamos el agente
   # st.write(type(MovieAgent))
    #logger.info("punto de control 4")

