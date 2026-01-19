from sqlalchemy import String,TIMESTAMP,Boolean
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class FollowUp(UUIDModel, TimestampedModel):
    followUpMessage:Mapped[str] = mapped_column(String)
    sendTime:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))