from bson import ObjectId
from fastapi.encoders import jsonable_encoder

from configuration import db
from src.schemas.payment import PaymentSchema


async def create_payment(payment: PaymentSchema):
    collection = db["payments"]
    payment_dict = jsonable_encoder(payment)
    new_payment = collection.insert_one(payment_dict)
    created_payment = collection.find_one({"_id": new_payment.inserted_id})
    return created_payment


async def register_payment(payment_id: str, status: str):
    collection = db["payments"]
    payment_updated = await collection.update_one(
        {"_id": ObjectId(payment_id)},
        {
            "$set": {
                "status": status
            }
        }
    )

    return payment_updated


async def get_payments():
    collection = db["payments"]
    payments_found = collection.find({})
    return payments_found
