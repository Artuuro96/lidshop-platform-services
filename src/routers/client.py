from typing import List

from fastapi import APIRouter, status
from src.models.client import Client
from src.repositories.client import (
    create_client,
    get_client_by_id,
    get_all_clients,
    update_client_by_id,
    delete_client_by_id
)
from src.schemas.client import ClientSchema

router = APIRouter()


@router.post("", response_model=Client, status_code=status.HTTP_201_CREATED)
async def create(client: ClientSchema):
    new_client = await create_client(client)
    return new_client


@router.get("/{client_id}", response_model=Client)
async def get_by_id(client_id):
    client_found = await get_client_by_id(client_id)
    return client_found


@router.get("", response_model=List[Client])
async def get_all():
    clients = await get_all_clients()
    return clients


@router.put("/{client_id}", response_model={})
async def update_by_id(client_id: str, client):
    client_updated = await update_client_by_id(client_id, client)
    print("===========>>>>>>", client_updated)
    return {}


@router.delete("/", response_model={}, status_code=status.HTTP_204_NO_CONTENT)
async def delete_by_id(client_id: str):
    await delete_client_by_id(client_id)
    return {}
