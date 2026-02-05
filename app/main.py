from fastapi import FastAPI
# Importamos schemas y crud para mantener la lógica organizada
from app import schemas, crud

app = FastAPI(
    title="🚀 Sistema de Ventas Pro - J4rly Corp",
    description="""
    ## Bienvenida al Portal de Inventarios
    Este sistema gestiona el flujo de productos con **Seguridad DevSecOps** integrada.
    
    * **Protección🛡️**: Código validado contra vulnerabilidades.
    * **Automatización📦**: Despliegue continuo mediante contenedores Docker.
    """,
    version="2.0.0",
    contact={
        "name": "Jorly - Lead DevOps Engineer",
        "url": "https://github.com/J4rly",
    }
)

@app.get("/", tags=["Estado"])
def root():
    """Confirma el estado operativo del núcleo del sistema."""
    return {
        "status": "ONLINE ✅",
        "entorno": "Entorno Local 💻",
        "seguridad": "Bandit Verified 🛡️",
        "mensaje": "Bienvenido al núcleo del Sistema de Ventas"
    }

@app.get("/alerta-stock", tags=["Inventario"])
def verificar_stock_bajo():
    """Consulta de productos con stock crítico (Simulado)."""
    return [
        {"producto": "Laptop Gaming", "stock": 2, "accion": "PEDIR URGENTE"},
        {"producto": "Monitor 4K", "stock": 5, "accion": "VIGILAR"}
    ]

@app.post("/products/", response_model=schemas.ProductOut, tags=["Ventas"])
def create_product(product: schemas.ProductCreate):
    """Registra un nuevo producto en memoria temporal."""
    return crud.create_product(product)

@app.get("/products/", response_model=list[schemas.ProductOut], tags=["Ventas"])
def read_products():
    """Obtiene la lista de productos registrados en la sesión."""
    return crud.get_products()
