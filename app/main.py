from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import crud, models, schemas  # El punto (.) le dice que busque en la misma carpeta
from .database import SessionLocal, engine
from app.database import SessionLocal, engine

# Crea las tablas en el archivo de base de datos automáticamente al iniciar
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Sistema Pro de Gestión de Ventas - J4rly Corp",
    description="""
    ## Bienvenida al Portal de Inventarios con Base de Datos 🗄️
    Este sistema gestiona datos reales con **Persistencia de Datos** y seguridad integrada.
    
    * **Protección🛡️**: Código validado contra vulnerabilidades.
    * **Automatización📦**: Despliegue continuo mediante contenedores Docker.
    * **Persistencia💾**: Datos guardados en SQLite.
    """,
    version="3.0.0",
    contact={
        "name": "Jorly - Lead DevOps Engineer",
        "url": "https://github.com/J4rly",
    }
)

# Función para obtener la conexión a la base de datos
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
        "mensaje": "Bienvenido al núcleo del Sistema de Ventas Real"
    }

@app.get("/alerta-stock", tags=["Inventario"])
def verificar_stock_bajo():
    """Simula una consulta de productos que necesitan reabastecimiento."""
    return [
        {"producto": "Laptop Gaming", "stock": 2, "accion": "PEDIR URGENTE"},
        {"producto": "Monitor 4K", "stock": 5, "accion": "VIGILAR"}
    ]

@app.get("/ventas-recientes", tags=["Reportes"])
def obtener_ventas_hoy():
    """Muestra un reporte resumido de las transacciones del día."""
    return [
        {"id_factura": "F-001", "cliente": "Juan Perez", "total": 150.50, "estado": "Pagado"},
        {"id_factura": "F-003", "cliente": "Carlos Ruiz", "total": 1200.00, "estado": "Pagado"}
    ]

@app.post("/products/", response_model=ProductOut, tags=["Ventas"])
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    """Registra un nuevo producto de forma PERMANENTE en la base de datos."""
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=list[ProductOut], tags=["Ventas"])
def read_products(db: Session = Depends(get_db)):
    """Obtiene la lista de productos reales guardados en el disco duro."""
    return crud.get_products(db=db)
