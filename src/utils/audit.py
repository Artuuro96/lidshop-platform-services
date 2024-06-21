from datetime import datetime
from typing import Optional

from pydantic import Field


class Audit:
    created_at: datetime = Field(alias="createdAt")
    created_by: str = Field(alias="createdBy")
    updated_at: datetime = Field(alias="updatedAt")
    updated_by: str = Field(alias="updatedBy")
    deleted_at: Optional[datetime] = Field(alias="deletedAt", default=datetime.now())
    deleted_by: Optional[str] = Field(alias="deletedBy", default=None)
    deleted: bool = Field(default=False)
