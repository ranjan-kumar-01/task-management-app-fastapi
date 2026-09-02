from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.tasks import controller
from src.tasks.dtos import TaskResponseSchema, TaskSchema
from src.utils.db import get_db

task_routes = APIRouter(prefix="/tasks")
db_dependency = Depends(get_db)


@task_routes.post(
    "/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_task(body: TaskSchema, db: Session = db_dependency):
    return controller.create_task(body, db)


@task_routes.get(
    "/all_task", response_model=list[TaskResponseSchema], status_code=status.HTTP_200_OK
)
def get_all_task(db: Session = db_dependency):
    return controller.get_task(db)


@task_routes.get(
    "/one_task/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_200_OK,
)
def get_one_task(task_id: int, db: Session = db_dependency):
    return controller.get_one_task(task_id, db)


@task_routes.patch(
    "/update/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def update_task(body: TaskSchema, task_id: int, db: Session = db_dependency):
    return controller.update_task(body, task_id, db)


@task_routes.delete(
    "/delete/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
def delete_one_task(task_id: int, db: Session = db_dependency):
    return controller.delete_task(task_id, db)
