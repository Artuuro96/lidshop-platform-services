from datetime import datetime, timezone

from src.models.article import Article
from typing import List, Optional
from pydantic import BaseModel, Field

from src.utils.audit import Audit


class ScheduledPayment(BaseModel):
    date_to_pay: str = Field(alias="dateToPay")
    quantity: float


class SaleSchema(BaseModel):
    sale_id: str = Field(alias="saleId")
    advance: float
    articles: List[Optional[Article]]
    debt: float
    frequencyPayment: str
    payment_method: str = Field(alias="paymentMethod")
    payments_number: float = Field(alias="paymentsNumber")
    total: float
    type: str
    status: str
    client_id: Optional[str] = Field(alias="clientId")
    vendor_id: Optional[str] = Field(alias="vendorId")
    scheduled_payments: List[ScheduledPayment] = Field(alias="scheduledPayments")
    created_at: datetime = Field(alias="createdAt", default_factory=lambda: datetime.now(timezone.utc))
    created_by: str = Field(alias="createdBy", default=None)
    updated_at: datetime = Field(alias="updatedAt", default_factory=lambda: datetime.now(timezone.utc))
    updated_by: str = Field(alias="updatedBy", default=None)
    deleted_at: Optional[datetime] = Field(alias="deletedAt", default=None)
    deleted_by: Optional[str] = Field(alias="deletedBy", default=None)
    deleted: bool = Field(default=False)
