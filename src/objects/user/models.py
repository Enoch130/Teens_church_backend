from sqlalchemy import String
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class Homepage(UUIDModel, TimestampedModel):
    title:Mapped[str] = mapped_column(String, nullable=False)
    subtitle:Mapped[str] = mapped_column(String, nullable=False)