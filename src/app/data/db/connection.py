from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Carga las variables de entorno
load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT', 5432) # Puerto por defecto de PostgreSQL
db_name = os.getenv('DB_NAME')

# Imprimir para depuración
print(f"Connecting to PostgreSQL with the following details:")
print(f"User: {user}")
print(f"Password: {password}")
print(f"Port: {port}")
print(f"Database Name: {db_name}")

# Formatear la URL de la base de datos
DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@postgres:{port}/{db_name}"

# Crear el engine de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Creamos el factory para las sesiones
SessionLocal = sessionmaker(bind=engine)

def get_db():
    """Crea y devuelve una sesión de base de datos para consultas"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
