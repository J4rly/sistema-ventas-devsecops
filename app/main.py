from fastapi import FastAPI
from app.schemas import ProductCreate, ProductOut
from app import crud

app = FastAPI(
    title="🚀 Sistema de Ventas Pro - J4rly and Darly Corp",
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
)

@app.get("/", tags=["Estado"])
def root():
    """Confirma el estado operativo del núcleo del sistema."""
    return {
        "status": "ONLINE ✅",
        "entorno": "Docker Container ",
        "seguridad": "Bandit Verified ",
        "mensaje": "Bienvenido al núcleo del Sistema de Ventas"
    }

@app.get("/alerta-stock", tags=["Inventario"])
def verificar_stock_bajo():
    """Consulta simulada de productos con stock crítico."""
    return [
        {"producto": "Laptop Gaming", "stock": 2, "accion": "PEDIR URGENTE"},
        {"producto": "Monitor 4K", "stock": 5, "accion": "VIGILAR"}
    ]

@app.get("/ventas-recientes", tags=["Reportes"])
def obtener_ventas_hoy():
    """Reporte resumido de las transacciones del día."""
    return [
        {"id_factura": "F-001", "cliente": "Juan Perez", "total": 150.50, "estado": "Pagado"},
        {"id_factura": "F-003", "cliente": "Carlos Ruiz", "total": 1200.00, "estado": "Pagado"}
    ]

@app.post("/products/", response_model=ProductOut, tags=["Ventas"])
def create_product(product: ProductCreate):
    """Registra un nuevo producto en la memoria temporal."""
    return crud.create_product(product)

@app.get("/products/", response_model=list[ProductOut], tags=["Ventas"])
def read_products():
    """Obtiene la lista de productos registrados en la sesión actual."""
    return crud.get_products()

