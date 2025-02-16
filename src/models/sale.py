from src.utils.audit import Audit
from typing import Annotated, List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from src.utils.util import ObjectIdPydanticAnnotation
from src.models.article import Article


class Sale(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(alias="_id")
    articles: List[Article] = Field(alias="articles")
    total: float
    type: str
    
    client_id: Optional[str] = Field(alias="clientId")
    vendor_id: Optional[str] = Field(alias="vendorId")
