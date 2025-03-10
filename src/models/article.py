from typing import Annotated, Literal, Optional, List
from pydantic import BaseModel, Field
from bson import ObjectId

from src.models.brand import Brand
from src.utils.util import ObjectIdPydanticAnnotation


class Article(BaseModel):
    id: Annotated[ObjectId, ObjectIdPydanticAnnotation] = Field(alias="_id")
    name: str
    code: str
    tax: float
    ticket_price: float = Field(alias="ticketPrice")
    parcel: float
    url: str
    lid_shop_price: float = Field(alias="lidShopPrice")
    other_costs: float = Field(alias="otherCosts")
    profit: float
    status: Literal["AVAILABLE", "RESERVED", "SOLD_OUT"]
    brand_id: str = Field(alias="brandId")


class ArticleDetail(BaseModel):
    id: str = Field(alias="_id")
    name: str
    code: str
    tax: float
    ticket_price: float = Field(alias="ticketPrice")
    parcel: float
    lid_shop_price: float = Field(alias="lidShopPrice")
    other_costs: float = Field(alias="otherCosts")
    profit: float
    status: Literal["AVAILABLE", "RESERVED", "SOLD_OUT"]
    brand: Brand


class ArticleResponseDeleted(BaseModel):
    deleted_ids: List[str] = Field(alias="deletedIds")
