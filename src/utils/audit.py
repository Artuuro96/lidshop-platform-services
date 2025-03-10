from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


class Audit(BaseModel):
    created_at: datetime = Field(alias="createdAt")
    created_by: str = Field(alias="createdBy")
    updated_at: datetime = Field(alias="updatedAt", default=None)
    updated_by: str = Field(alias="updatedBy", default=None)
    deleted_at: Optional[datetime] = Field(alias="deletedAt", default=None)
    deleted_by: Optional[str] = Field(alias="deletedBy", default=None)
    deleted: bool = Field(default=False)
