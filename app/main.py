from fastapi import FastAPI
from app.schemas import ProductCreate, ProductOut
from app import crud

app = FastAPI(
    title="Sistema Pro de Gestión de Ventas - J4rly Corp",
    description="""
    ## Bienvenida al Portal de Inventarios
    Este sistema gestiona el flujo de productos con **Seguridad DevSecOps** integrada.
    
    * **Protección**: Código validado contra vulnerabilidades.
    * **Automatización**: Despliegue continuo mediante contenedores Docker.
    """,
    version="2.0.0",
    contact={
        "name": "Jorly - Lead DevOps Engineer",
        "url": "https://github.com/J4rly",
    }
) # <--- EL PARÉNTESIS DEBE CERRAR AQUÍ

@app.get("/", tags=["Estado"])
def root():
    """Confirma el estado operativo del núcleo del sistema."""
    return {
        "status": "ONLINE ",
        "entorno": "Docker Container ",
        "seguridad": "Bandit Verified ",
        "mensaje": "Bienvenido al núcleo del Sistema de Ventas"
    }

@app.get("/alerta-stock", tags=["Inventario"])
def verificar_stock_bajo():
    """Simula una consulta de productos que necesitan reabastecimiento urgente."""
    return [
        {"producto": "Laptop Gaming", "stock": 2, "accion": "PEDIR URGENTE"},
        {"producto": "Monitor 4K", "stock": 5, "accion": "VIGILAR"}
    ]

@app.post("/products/", response_model=ProductOut, tags=["Ventas"])
def create_product(product: ProductCreate):
    """Registra un nuevo producto en el sistema de ventas."""
    return crud.create_product(product)

@app.get("/products/", response_model=list[ProductOut], tags=["Ventas"])
def read_products():
    """Obtiene la lista completa de productos registrados."""
    return crud.get_products()
)
