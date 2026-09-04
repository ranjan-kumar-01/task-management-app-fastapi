from pydantic import BaseModel


class UserSchema(BaseModel):
    name: str
    username: str
    password: str
    email: str


class UserResponseSchema(BaseModel):
    name: str
    username: str
    email: str
    id: int

    model_config = {
        "from_attributes": True
    }


class LoginSchema(BaseModel):
    username: str
    password: str
