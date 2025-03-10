from typing import List

from fastapi import APIRouter, HTTPException, status, Depends, Query

from src.auth.auth import auth_request
from src.models.article import Article
from src.models.sale import Sale
from src.repositories.payment import create_payment
from src.schemas.article import ArticleSchema
from src.schemas.payment import PaymentSchema
from src.schemas.sale import SaleSchema
from src.repositories.article import get_article_by_id, update_article, delete_article
from src.repositories.sale import create_sale, get_sales, get_sales_by_id, get_last_sale, delete_sales_by_ids
from src.services.email import send_email

router = APIRouter()


@router.get("", response_model=List[Sale])
async def get_all():
    articles = await get_sales()
    return articles


@router.post("", response_model=Sale)
async def create(sale: SaleSchema, execution_ctx: dict = Depends(auth_request)):
    for article in sale.articles:
        article_found = await update_article(str(article.id), {"status": "SOLD_OUT"})
        if not article_found:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, f"Article {article.id} does not exist")

    new_sale = await create_sale(sale, execution_ctx["sub"])
    scheduled_payments = []
    for i, scheduled_payment in enumerate(sale.scheduled_payments):
        new_payment = PaymentSchema(
            number=i,
            quantity=scheduled_payment.quantity,
            date_to_pay=scheduled_payment.date_to_pay,
            client_id=sale.client_id,
            sale_id=str(new_sale["_id"]),
            status="PENDING"
        )
        scheduled_payments.append(new_payment)
        await create_payment(new_payment)
    await send_email(new_sale)
    return new_sale


@router.get("/{sale_id}", response_model=Sale)
async def get_by_id(sale_id: str) -> Sale:
    sale = await get_sales_by_id(sale_id)
    return sale


@router.delete("/", status_code=status.HTTP_200_OK, response_model=List[str])
async def delete_by_ids(article_ids: List[str] = Query(...)):
    deleted_ids = await delete_sales_by_ids(article_ids)
    return {
        "deletedIds": deleted_ids
    }
