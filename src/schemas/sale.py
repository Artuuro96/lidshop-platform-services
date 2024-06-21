from src.utils.audit import Audit
from typing import List
from pydantic import BaseModel, Field


class SaleSchema(BaseModel, Audit):
    article_ids: List[str] = Field(alias="articleIds")
    total: float
    client_id: str
    vendor_id: str
