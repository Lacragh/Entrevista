# FastAPI Project (Estructura)


### Ejecutar proyecto

# Ejecutar en la consola el siguiente comando 
uvicorn app.app:app --reload

## isntalar dependencias
pip install -r requirements.txt
```

Open:
- API root: http://127.0.0.1:8000/
- Docs (Swagger UI): http://127.0.0.1:8000/docs


## Correr con docker

Prerequisitos: tener Docker Desktop instalado y en ejecución.


```


### Usando Docker Compose 

```powershell
docker compose up --build
```

Esto usa `docker-compose.yml` para:
- Montar el código local dentro del contenedor (hot-reload con `--reload`).
- Cargar variables desde `.env` (opcional).
- Exponer 8000 en tu máquina.










