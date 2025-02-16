from src.utils.audit import Audit
from typing import Annotated, List
from bson import ObjectId
from pydantic import BaseModel, Field
from src.utils.util import ObjectIdPydanticAnnotation


class Sale(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(alias="_id")
    articles: List[str] = Field(alias="articleIds")
    total: float
    client_id: str
    vendor_id: str
