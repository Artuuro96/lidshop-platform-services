from fastapi import APIRouter, HTTPException, status
from src.models.sale import Sale
from src.schemas.sale import SaleSchema
from src.repositories.article import get_article_by_id
from src.repositories.sale import create_sale

router = APIRouter()


@router.post("/", response_model=Sale)
async def create(sale: SaleSchema):
    for article_id in sale.article_ids:
        article_found = await get_article_by_id(article_id)
        if not article_found:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, f"Article {article_id} does not exist")

    new_sale = await create_sale(sale)
    return new_sale
