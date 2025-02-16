from typing import List

from bson import ObjectId

from src.models.sale import Sale
from src.schemas.sale import SaleSchema
from configuration import db
from fastapi.encoders import jsonable_encoder


async def create_sale(sale: SaleSchema):
    collection = db["sales"]
    sale_dict = jsonable_encoder(sale)
    new_sale = collection.insert_one(sale_dict)
    created_sale = collection.find_one({"_id": new_sale.inserted_id})
    return created_sale


async def get_sales() -> List[Sale]:
    collection = db["sales"]
    sales = collection.find({})
    return sales


async def get_sales_by_id(sale_id: str) -> Sale:
    collection = db["sales"]
    sale = collection.find_one({"_id": ObjectId(sale_id)})
    return sale
