from typing import List
from configuration import db
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, status
from bson import ObjectId
from src.models.brand import Brand
from src.schemas.brand import BrandSchema


async def create_brand(brand: BrandSchema) -> Brand:
    collection = db["brands"]
    brand_dict = jsonable_encoder(brand)
    new_brand = collection.insert_one(brand_dict)
    brand_created = collection.find_one({"_id": ObjectId(new_brand.inserted_id)})
    return brand_created


async def get_all_brands() -> List[Brand]:
    collection = db["brands"]
    brands_found = collection.find({})
    return brands_found


async def get_brand_by_id(brand_id: str) -> Brand:
    collection = db["brands"]
    brand_found = collection.find_one({
        "_id": ObjectId(brand_id)
    })

    if not brand_found:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Brand {brand_id} not found")
    return brand_found


async def update_brand_by_id(brand_id: str, brand: Brand) -> Brand:
    collection = db["brands"]
    brand_found = collection.update_one({
        "_id": ObjectId(brand_id)
    }, {
        "$set": brand
    })
    return brand_found


async def delete_brand_by_id(brand_id: str):
    collection = db["brands"]
    result = collection.delete_one({"_id": ObjectId(brand_id)})
    return result
