from typing import Optional, Annotated

from bson import ObjectId
from pydantic import BaseModel, Field
from src.utils.util import ObjectIdPydanticAnnotation


class Client(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(alias="_id")
    name: str
    last_name: str = Field(alias="lastName")
    email: str
    points: float
    age: int
    address: str
    cellphone: str
