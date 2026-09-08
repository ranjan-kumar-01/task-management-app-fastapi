from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.tasks import controller
from src.tasks.dtos import TaskResponseSchema, TaskSchema
from src.tasks.models import TaskModel
from src.user.models import UserModel
from src.utils.db import get_db
from src.utils.helper import is_authenticated

from src.utils.auth import security

task_routes = APIRouter(prefix="/task")

# Reusable database dependency.
db_dependency = Annotated[Session, Depends(get_db)]

user_dependency = Annotated[UserModel, Depends(is_authenticated)]


@task_routes.post(
    "/create", response_model=TaskResponseSchema, status_code=status.HTTP_201_CREATED
)
def create_task(
    body: TaskSchema, db: db_dependency, user: user_dependency
) -> TaskModel:
    return controller.create_task(body, db, user)


@task_routes.get(
    "/all_task", response_model=list[TaskResponseSchema], status_code=status.HTTP_200_OK
)
def get_all_task(db: db_dependency, user: user_dependency, credentials=Depends(security)) -> list[TaskModel]:
    return controller.get_task(db, user)


@task_routes.get(
    "/one_task/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_200_OK,
)
def get_one_task(task_id: int, db: db_dependency, user: user_dependency) -> TaskModel:
    return controller.get_one_task(task_id, db)


@task_routes.patch(
    "/update/{task_id}",
    response_model=TaskResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def update_task(
    body: TaskSchema, task_id: int, db: db_dependency, user: user_dependency
) -> TaskModel:
    return controller.update_task(body, task_id, db, user)


@task_routes.delete(
    "/delete/{task_id}", response_model=None, status_code=status.HTTP_204_NO_CONTENT
)
def delete_one_task(task_id: int, db: db_dependency, user: user_dependency) -> None:
    return controller.delete_task(task_id, db, user)
