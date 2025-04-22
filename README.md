# 🎥 **Proyecto_LLM_ChatbotRecomendation** 🎥

**¡Bienvenido al proyecto de recomendación de películas!**  
Este chatbot está diseñado para **recomendar películas** basándose en tus **gustos** y **emociones**. 🎥✨  

Para lograr esto, hemos implementado:  
- Una **base de datos vectorial** que permite **recomendaciones personalizadas**.  
- Una **base de datos relacional** para responder consultas sobre los **premios Óscar**.  
  🏆 ¿Tienes dudas sobre los ganadores? ¡El chatbot tiene las respuestas!  
- La **API de TMDB** para ofrecer información adicional como:  
  - 🎞️ **Películas en cartelera**  
  - 📺 **Mejores series de la historia**  
  - 🍿 **Mejores películas de la historia**  

---

## 🚀 **Pasos para deployar el proyecto**

Sigue estos pasos para configurar y desplegar el proyecto correctamente:

### 1️⃣ **Crear el archivo `.env`**
Crea un archivo llamado `.env` en la raíz del proyecto. Este archivo almacenará las credenciales necesarias para que el proyecto funcione correctamente. A continuación, se muestran los campos que deben incluirse en el archivo `.env`:

```env
# Configuraciones de Langsmith (Opcional)
LANGCHAIN_TRACING_V2=
LANGCHAIN_ENDPOINT=""
LANGCHAIN_API_KEY=""
LANGCHAIN_PROJECT=""

# Configuraciones de OpenAI
OPENAI_API_KEY=""

# Configuraciones de TMDB API
account=""
API_KEY_TMDB=""

# Configuraciones de PostgreSQL
DB_USER=""
DB_PASSWORD=""
DB_HOST="postgres"
DB_PORT=5432
DB_NAME=""

## **Dataset utilizado**  
📂 [TMDb Movies Dataset 2023 - 930k Movies](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies)

