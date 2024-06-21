from src.schemas.sale import SaleSchema
from configuration import db
from fastapi.encoders import jsonable_encoder


async def create_sale(sale: SaleSchema):
    collection = db["sales"]
    sale_dict = jsonable_encoder(sale)
    new_sale = collection.insert_one(sale_dict)
    created_sale = collection.find_one({"_id": new_sale.inserted_id})
    return created_sale
