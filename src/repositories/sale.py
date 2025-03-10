from typing import List
from bson import ObjectId
from fastapi import HTTPException

from src.models.sale import Sale
from src.schemas.sale import SaleSchema
from configuration import db
from fastapi.encoders import jsonable_encoder

from src.utils.setaudit import set_audit_values


async def create_sale(sale: SaleSchema, user_id: str):
    collection = db["sales"]
    sale_dict = jsonable_encoder(sale)
    sale_dict["createdBy"] = user_id
    sale_dict["updatedBy"] = user_id
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


async def get_last_sale() -> Sale:
    collection = db["sales"]
    sale = collection.find_one({})
    return sale


async def delete_sales_by_ids(sale_ids: List[str]):
    collection = db["sales"]
    result = []
    for sale_id in sale_ids:
        deleted_result = collection.delete_one({"_id": ObjectId(sale_id)})
        if deleted_result.deleted_count == 1:
            result.append(sale_id)
        else:
            raise HTTPException(status_code=404, detail=f"{sale_id} not found")

    return result
