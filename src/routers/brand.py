from typing import List

from fastapi import APIRouter, status
from src.models.brand import Brand
from src.schemas.brand import BrandSchema
from src.repositories.brand import (
    get_all_brands,
    get_brand_by_id,
    create_brand,
    update_brand_by_id,
    delete_brand_by_id
)

router = APIRouter()


@router.get("", response_model=List[Brand])
async def get_all() -> List[Brand]:
    brands_found = await get_all_brands()
    return brands_found


@router.get("/{brand_id}", response_model=Brand)
async def get_by_id(brand_id) -> Brand:
    brand_found = await get_brand_by_id(brand_id)
    return brand_found


@router.post("", response_model=Brand, status_code=status.HTTP_201_CREATED)
async def create(brand: BrandSchema) -> Brand:
    new_brand = await create_brand(brand)
    return new_brand


@router.put("/{brand_id}", response_model=Brand)
async def update_by_id(brand_id: str, brand: Brand) -> Brand:
    update_brand = await update_brand_by_id(brand_id, brand)
    return update_brand


@router.delete("/{brand_id", response_model={}, status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(brand_id: str):
    await delete_brand_by_id(brand_id)
    return {}

