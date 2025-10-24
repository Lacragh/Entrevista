from fastapi import FastAPI
from app.routes import items

app = FastAPI(title="API REST PRUEBA ENTREVISTA")

# Registrar las rutas
app.include_router(items.router)

# Correr con: uvicorn app.app:app --reload
