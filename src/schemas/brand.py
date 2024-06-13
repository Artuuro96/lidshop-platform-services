from typing import Optional

from pydantic import BaseModel


class BrandSchema(BaseModel):
    name: str
    description: Optional[str]
    acronym: Optional[str]
