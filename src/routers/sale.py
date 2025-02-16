from typing import List

from fastapi import APIRouter, HTTPException, status
from src.models.sale import Sale
from src.schemas.sale import SaleSchema
from src.repositories.article import get_article_by_id
from src.repositories.sale import create_sale, get_sales, get_sales_by_id

router = APIRouter()


@router.get("/", response_model=List[Sale])
async def get_all():
    articles = await get_sales()
    return articles


@router.post("/", response_model=Sale)
async def create(sale: SaleSchema):
    for article in sale.articles:
        article_found = await get_article_by_id(article.id)
        if not article_found:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, f"Article {article_id} does not exist")

    new_sale = await create_sale(sale)
    return new_sale


@router.get("/{sale_id}", response_model=Sale)
async def get_by_id(sale_id: str) -> Sale:
    sale = await get_sales_by_id(sale_id)
    return sale
