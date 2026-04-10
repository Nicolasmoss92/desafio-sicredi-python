from fastapi import FastAPI

from app.routers.orders import router as orders_router
from app.routers.contracts import router as contracts_router

app = FastAPI(
    title="Desafio Técnico Python",
    description="Solução do desafio técnico Sicredi.",
    version="1.0.0",
)

app.include_router(contracts_router)
app.include_router(orders_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}