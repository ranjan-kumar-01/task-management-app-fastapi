from typing import Annotated

from fastapi import APIRouter, Depends, Request, status
from sqlalchemy.orm import Session

from src.user import controller
from src.user.dtos import LoginSchema, UserResponseSchema, UserSchema
from src.user.models import UserModel
from src.utils.db import get_db

user_routes = APIRouter(prefix="/user")

# Reusable database dependency.
db_dependency = Annotated[Session, Depends(get_db)]


@user_routes.post(
    "/register", response_model=UserResponseSchema, status_code=status.HTTP_201_CREATED
)
async def register(body: UserSchema, db: db_dependency) -> UserModel:
    return await controller.register(body, db)


@user_routes.post("/login", status_code=status.HTTP_200_OK)
def login(body: LoginSchema, db: db_dependency) -> dict[str, str]:
    return controller.login(body, db)


@user_routes.get("/is_auth", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
def is_auth(request: Request, db: db_dependency) -> UserModel:
    return controller.is_authenticated(request, db)
