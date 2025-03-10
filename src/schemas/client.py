from pydantic import BaseModel, Field


class ClientSchema(BaseModel):
    name: str
    last_name: str = Field(alias="lastName")
    email: str
    points: float
    age: int
    address: str
    cellphone: str
