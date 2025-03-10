from datetime import datetime, timezone
from typing import Annotated, Optional, Literal

from bson import ObjectId
from pydantic import BaseModel, Field

from src.utils.util import ObjectIdPydanticAnnotation


class PaymentSchema(BaseModel):
    number: int
    quantity: float
    client_id: str
    sale_id: str
    date_to_pay: str = Field("dateToPay")
    status: Literal["PENDING", "VALIDATING", "DELAYED", "CONFIRMED"]
    created_at: datetime = Field(alias="createdAt", default=datetime.now(timezone.utc))
    created_by: str = Field(alias="createdBy", default=None)
    updated_at: datetime = Field(alias="updatedAt", default=datetime.now(timezone.utc))
    updated_by: str = Field(alias="updatedBy", default=None)
    deleted_at: Optional[datetime] = Field(alias="deletedAt", default=None)
    deleted_by: Optional[str] = Field(alias="deletedBy", default=None)
    deleted: bool = Field(default=False)
