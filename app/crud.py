# Lista temporal que vive solo mientras el servidor esté encendido
products_db = []

def get_products():
    """Retorna la lista de productos guardados en memoria."""
    return products_db

def create_product(product):
    """Registra un nuevo producto en la lista temporal."""
    # Creamos un diccionario con los datos del producto
    new_product = {
        "id": len(products_db) + 1,
        "name": product.name,
        "price": product.price,
        "stock": product.stock
    }
    products_db.append(new_product)
    return new_product
