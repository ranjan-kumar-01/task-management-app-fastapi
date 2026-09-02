from fastapi import FastAPI

from src.tasks.router import task_routes
from src.utils.db import Base, engine

Base.metadata.create_all(engine)
app = FastAPI(title="Task Management App With FastApi")
app.include_router(task_routes)
