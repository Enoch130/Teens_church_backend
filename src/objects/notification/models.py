from sqlalchemy import String,TIMESTAMP,Boolean
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Notification(UUIDModel, TimestampedModel):
    reminderType:Mapped[str] = mapped_column(String)
    messageTemplate:Mapped[str] = mapped_column(String)
    sendTime:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
