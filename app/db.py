from fastapi import FastAPI
from app import schemas, crud

app = FastAPI(title="Sistema de Ventas Pro - J4rly")

@app.get("/")
def root():
    return {"message": "SISTEMA ONLINE ✅", "database": "Memoria Volátil"}

@app.post("/products/", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate):
    return crud.create_product(product)

@app.get("/products/", response_model=list[schemas.ProductOut])
def read_products():
    return crud.get_products()
