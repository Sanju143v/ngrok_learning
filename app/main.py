from fastapi import FastAPI

from app.db.database import Base, engine
from app.routes.users import router as users_router

app = FastAPI(title="FastAPI User Service")

app.include_router(users_router, prefix="/users", tags=["users"])


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Hello, World from FastAPI"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
