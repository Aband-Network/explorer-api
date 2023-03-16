from fastapi import FastAPI
from broadcaster import Broadcast

from app.settings import settings

broadcast = Broadcast("redis://127.0.0.1:6379")

app = FastAPI(
    on_startup=[broadcast.connect], on_shutdown=[broadcast.disconnect]
)
