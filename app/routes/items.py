from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional


router = APIRouter(prefix="/items", tags=["Items"])

# Modelo de datos
class Item(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float


items_db = []  # Lista para almacenar los items creados temporalmente
counter = 1    # Contador para asignar a cada item el id


# POST /items - Crear un nuevo ítem
@router.post("/")
def crear_item(item: Item):
    global counter
    item.id = counter
    counter += 1
    items_db.append(item)
    return {"mensaje": "Item creado exitosamente", "item": item}


# GET /items - Devolver todos los ítems
@router.get("/")
def obtener_items():
    return items_db

# (Opcional) GET /items/{id} - Devolver ítem por ID
@router.get("/{id}")
def obtener_item_por_id(id: int):
    for item in items_db:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Item no encontrado")
