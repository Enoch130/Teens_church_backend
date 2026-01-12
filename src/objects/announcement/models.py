from sqlalchemy import String,TIMESTAMP,Boolean
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Announcement(UUIDModel, TimestampedModel):
    title:Mapped[str] = mapped_column(String)
    message:Mapped[str] = mapped_column(String)
    channel:Mapped[str] = mapped_column(String)
    scheduleAt:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))