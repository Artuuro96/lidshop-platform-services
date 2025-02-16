from src.models.article import Article
from typing import List, Optional
from pydantic import BaseModel, Field


class ScheduledPayment(BaseModel):
    date_to_pay: str = Field(alias="dateToPay")
    quantity: float


class SaleSchema(BaseModel):
    advance: float
    articles: List[Optional[Article]]
    debt: float
    frequencyPayment: str
    paymentMethod: str
    paymentsNumber: int
    total: float
    type: str
    client_id: Optional[str] = Field(alias="clientId")
    vendor_id: Optional[str] = Field(alias="vendorId")
