from typing import Optional

from configuration import db
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException
from bson import ObjectId
from src.models.client import Client
from src.schemas.client import ClientSchema


async def create_client(client: ClientSchema) -> Client:
    collection = db["clients"]
    client_dict = jsonable_encoder(client)
    new_client = collection.insert_one(client_dict)
    created_client = collection.find_one({"_id": new_client.inserted_id})
    return created_client


async def get_client_by_id(client_id: str):
    collection = db["clients"]
    client_found = collection.find_one({
        "_id": ObjectId(client_id)
    })
    if not client_found:
        raise HTTPException(status_code=404, detail=f"Client ${client_id} not found")
    return client_found


async def get_all_clients():
    collection = db["clients"]
    clients = collection.find({})
    return clients


async def update_client_by_id(client_id: str, client: Optional[ClientSchema]):
    collection = db["clients"]
    client_dict = jsonable_encoder(client)
    result = collection.update_one({
        "_id": ObjectId(client_id)
    }, {
        "$set": client_dict
    })
    if result.matched_count == 1:
        return result


async def delete_client_by_id(client_id: str):
    collection = db["clients"]
    result = collection.delete_one({
        "_id": ObjectId(client_id)
    })
    return result
