# Usa una imagen oficial de Python como base
FROM python:3.10-slim

# Establece el directorio de trabajo dentro del contenedor
RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y build-essential
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Copia el archivo de requirements al contenedor
COPY . /code

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente de la carpeta raíz (que incluye "app" y "stream")


# Expone el puerto que Streamlit usará
EXPOSE 8501

# Define el comando para ejecutar Streamlit, usando el archivo dentro de "stream"
CMD ["streamlit", "run", "stream/moviechat.py", "--server.port=8501", "--server.address=0.0.0.0"]