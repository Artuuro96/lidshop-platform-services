from datetime import datetime
from typing import Annotated, Literal, Optional

from bson import ObjectId
from pydantic import BaseModel, Field

from src.utils.util import ObjectIdPydanticAnnotation


class Payment(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(alias="_id")
    quantity: float
    client_id: str
    sale_id: str
    date_to_pay: str = Field("dateToPay")
    status: Literal["PENDING", "VALIDATING", "DELAYED", "CONFIRMED"]
    created_at: datetime = Field(alias="createdAt")
    created_by: Optional[str] = Field(alias="createdBy")
    updated_at: datetime = Field(alias="updatedAt")
    updated_by: Optional[str] = Field(alias="updatedBy")
    deleted_at: Optional[datetime] = Field(alias="deletedAt")
    deleted_by: Optional[str] = Field(alias="deletedBy")
    deleted: bool
