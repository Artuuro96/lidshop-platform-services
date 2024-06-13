from typing import Optional
from pydantic import BaseModel, Field


class ClientSchema(BaseModel):
    name: str
    last_name: str
    email: str
    points: float
    age: int
    address: str
    cellphone: str
