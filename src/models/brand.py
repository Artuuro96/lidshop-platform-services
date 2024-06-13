from typing import Optional, Annotated
from bson import ObjectId
from pydantic import BaseModel, Field
from src.utils.util import ObjectIdPydanticAnnotation


class Brand(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(alias="_id")
    name: str
    description: Optional[str]
    acronym: Optional[str]
