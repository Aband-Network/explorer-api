from fastapi import FastAPI

from app.settings import settings


app = FastAPI(
    title=settings.PROJECT_NAME
)
