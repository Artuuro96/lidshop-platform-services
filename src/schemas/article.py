from typing import Optional, Literal

from pydantic import BaseModel, Field


class ArticleSchema(BaseModel):
    name: str
    code: str
    tax: float
    ticket_price: float = Field(alias="ticketPrice")
    parcel: float
    lid_shop_price: float = Field(alias="lidShopPrice")
    other_costs: float = Field(alias="otherCosts")
    profit: float
    status: Literal["AVAILABLE", "RESERVED", "SOLD_OUT"]
    brand_id: Optional[str] = Field(alias="brandId")
