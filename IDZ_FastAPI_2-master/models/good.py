from typing import Union, Annotated
from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    email: str

class CreateUser(BaseModel):
    username: str
    email: str

