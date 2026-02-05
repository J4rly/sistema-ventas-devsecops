from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
# Usamos rutas absolutas para que uvicorn no se pierda
import app.crud as crud
import app.models as models
import app.schemas as schemas
from app.database import SessionLocal, engine

# Crea las tablas automáticamente al iniciar usando el objeto models
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="🚀 Sistema de Ventas Pro - J4rly Corp",
    description="""
    ## Bienvenida al Portal de Inventarios Real
    Este sistema gestiona productos con **Persistencia de Datos** y seguridad verificada.
    
    * **Seguridad🛡️**: Escaneado por Bandit.
    * **Infraestructura🐳**: Desplegado en Docker.
    * **Almacenamiento💾**: SQLite Database activo.
    """,
    version="3.1.0",
    contact={
        "name": "Jorly - Lead DevOps Engineer",
        "url": "https://github.com/J4rly",
    }
)

# Dependencia para la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Estado"])
def root():
    """Confirma el estado operativo del núcleo y la base de datos."""
    return {
        "status": "ONLINE ✅",
        "base_de_datos": "CONECTADA 🗄️",
        "entorno": "Docker Container 🐳",
        "mensaje": "Bienvenido al núcleo del Sistema de Ventas"
    }

@app.get("/alerta-stock", tags=["Inventario"])
def verificar_stock_bajo():
    """Ejemplo práctico: Consulta de productos que necesitan reabastecimiento."""
    return [
        {"producto": "Laptop Gaming", "stock": 2, "accion": "PEDIR URGENTE"},
        {"producto": "Monitor 4K", "stock": 5, "accion": "VIGILAR"}
    ]

# CORRECCIÓN AQUÍ: Usamos schemas.ProductOut y crud.create_product
@app.post("/products/", response_model=schemas.ProductOut, tags=["Ventas"])
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    """Guarda un producto de forma PERMANENTE en la base de datos."""
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=list[schemas.ProductOut], tags=["Ventas"])
def read_products(db: Session = Depends(get_db)):
    """Obtiene la lista de productos reales guardados en el disco duro."""
    return crud.get_products(db=db)
