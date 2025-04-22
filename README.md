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
DB_USER="postgres"
DB_PASSWORD="admin"
DB_HOST="postgres"
DB_PORT=5432
DB_NAME=""
```

1. **Langsmith**: Es opcional y solo necesario si deseas monitorear el proyecto utilizando esta herramienta.
2. **OpenAI API**: Proporciona la clave API de OpenAI para habilitar la funcionalidad del chatbot.
3. **TMDB API**: Incluye las credenciales necesarias para acceder a la API de TMDB.
4. **PostgreSQL**:
- Luego de Levantar el proyecto podrás ingresar a la bd con las credenciales del **docker-compose**, para luego crear la BD e importar el dataset.
  
 ![image](https://github.com/user-attachments/assets/0ecd0130-bc0d-4bb0-9365-95dd2e44a504)

- El valor de DB_NAME corresponde al nombre de la base de datos, que es de la preferencia del usuario.
- Importante: Asegúrate de importar toda la información del dataset **the_oscar_award_pgadmin.csv**, ubicado en la carpeta datasets, a esta base de datos. Este dataset contiene la información requerida para responder consultas relacionadas con los premios Óscar.

---

### 2️⃣ **Construir y ejecutar el proyecto**
Sigue estos pasos para iniciar el proyecto:

1. **Construir los contenedores Docker:**
   
   ```bash
   docker-compose build

2. **Iniciar los Servidores**

   ```bash
   docker-compose up

### 3️⃣ **Ingresar a PGADMIN**
1. **Luego de utilizar estos comandos, se te creará el container en docker y podrás ingresar a la plataforma de PGADMIN para crear la bd e importar los datos.**

![image](https://github.com/user-attachments/assets/736ad69f-dec0-4ed3-824e-deaa25ae5290)

2. **Dentro de la plataforma pones las credenciales, creas la bd y LISTO!**

![image](https://github.com/user-attachments/assets/b68c3b68-3bcf-444a-8311-9bb4e668d862)


##**Dataset utilizado**  
📂 [TMDb Movies Dataset 2023 - 930k Movies](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies)

