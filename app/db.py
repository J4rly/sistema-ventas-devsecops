from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL para MySQL (Usaremos pymysql como el "traductor")
# root:password es el ejemplo, cámbialo si tu servidor tiene otros datos
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/ventas_db"

# Creamos el motor de conexión
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Configuramos la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para crear tus tablas
Base = declarative_base()
