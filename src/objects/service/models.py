from sqlalchemy import String,TIMESTAMP,Boolean
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(UUIDModel, TimestampedModel):
    name:Mapped[str] = mapped_column(String)
    serviceDate:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
    serviceType:Mapped[str] = mapped_column(String)