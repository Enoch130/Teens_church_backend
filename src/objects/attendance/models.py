from sqlalchemy import String,TIMESTAMP,Boolean
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Attendance(UUIDModel, TimestampedModel):
    status:Mapped[str] = mapped_column(String)
    checkinTime:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))