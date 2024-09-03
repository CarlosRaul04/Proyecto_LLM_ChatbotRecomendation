import streamlit as st
from app import MovieAgent


# Configuración básica de la página
st.set_page_config(page_title="Recomendador de Películas", layout="centered")

st.title("Recomendador de Películas")

# Ejemplo de input del usuario
user_input = st.text_input("¿Qué tipo de película te gustaría ver hoy?")

if user_input:
    # Aquí va la lógica de recomendación de películas usando el chatbot
    # Por simplicidad, solo mostraremos el input del usuario
    st.write(f"Buscando películas que coincidan con: {user_input}")
    # Aquí puedes llamar a tu función de recomendación y mostrar resultados

    # Usamos el agente
    print(type(MovieAgent))
