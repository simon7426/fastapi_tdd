import logging
import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.api.ping import router
from app.db import init_db

log = logging.getLogger("uvicorn")

def create_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    return app

app = create_application()

@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)

@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")

