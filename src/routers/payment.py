from http.client import HTTPException
from typing import List

from fastapi import APIRouter, status

from src.models.payment import Payment
from src.repositories.payment import create_payment, register_payment, get_payments
from src.repositories.sale import get_sales_by_id
from src.schemas.payment import PaymentSchema

router = APIRouter()


@router.post("", response_model=Payment, status_code=status.HTTP_201_CREATED)
async def create(payment: PaymentSchema):
    sale_found = await get_sales_by_id(payment.sale_id)
    if not sale_found:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, f'Sale with id {payment.sale_id} not found')

    payment_created = await create_payment(payment)
    return payment_created


@router.patch("/register/{payment_id}", response_model=Payment, status_code=status.HTTP_200_OK)
async def register(payment_id: str):
    payment_updated = await register_payment(payment_id, "VALIDATING")
    return payment_updated


@router.get("", response_model=List[Payment], status_code=status.HTTP_200_OK)
async def get_all():
    payments_found = await get_payments()
    return payments_found
