from src.utils.audit import Audit
from typing import Annotated, List, Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from src.utils.util import ObjectIdPydanticAnnotation
from src.models.article import Article


class Sale(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(alias="_id")
    sale_id: str = Field(alias="saleId")
    advance: float
    articles: List[Article] = Field(alias="articles")
    debt: float
    payment_method: str = Field(alias="paymentMethod")
    payments_number: float = Field(alias="paymentsNumber")
    total: float
    type: str
    status: str
    client_id: Optional[str] = Field(alias="clientId")
    vendor_id: Optional[str] = Field(alias="vendorId")
    created_at: str = Field(alias="createdAt")
    created_by: str = Field(alias="createdBy")
    updated_at: str = Field(alias="updatedAt")
    updated_by: str = Field(alias="updatedBy")
    deleted_at: Optional[str] = Field(alias="deletedAt")
    deleted_by: Optional[str] = Field(alias="deletedBy")
    deleted: bool
