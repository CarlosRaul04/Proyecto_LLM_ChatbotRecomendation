import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from loguru import logger

logger.info("punto de control 1")
from app import MovieAgent

logger.info("punto de control 2")

# Configuración básica de la página
st.set_page_config(page_title="Recomendador de Películas", layout="centered")

st.title("Recomendador de Películas")

# Ejemplo de input del usuario
user_input = st.text_input("¿Qué tipo de película te gustaría ver hoy?")
print("antes del if")
logger.info("punto de control 3")
if user_input:
    print("dentro del if")
    # Aquí va la lógica de recomendación de películas usando el chatbot
    # Por simplicidad, solo mostraremos el input del usuario
    st.write(f"Buscando películas que coincidan con: {user_input}")
    # Aquí puedes llamar a tu función de recomendación y mostrar resultados

    # Usamos el agente
    print(type(MovieAgent))
    logger.info("punto de control 4")
