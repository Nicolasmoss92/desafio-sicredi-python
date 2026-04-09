from fastapi import FastAPI

from app.routers.orders import router as orders_router

app = FastAPI(
    title="Desafio Técnico Python",
    description="Solução do desafio técnico com FastAPI",
    version="1.0.0",
)

app.include_router(orders_router)