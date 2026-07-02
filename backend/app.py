from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from backend.routes import router

app = FastAPI(
    title="CADMS Backend",
    version="1.0"
)

app.include_router(router)

app.mount(
    "/static",
    StaticFiles(directory="backend/static"),
    name="static"
)