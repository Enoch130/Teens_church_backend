from sqlalchemy import String,TIMESTAMP,Boolean
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(UUIDModel, TimestampedModel):
    firstName:Mapped[str] = mapped_column(String)
    middleName:Mapped[str] = mapped_column(String, nullable=True)
    lastName:Mapped[str] = mapped_column(String)
    email:Mapped[str] = mapped_column(String,unique=True, index = True)
    phoneNumber:Mapped[str] = mapped_column(String)
    gender:Mapped[str] = mapped_column(String)
    isActive:Mapped[bool] = mapped_column(Boolean)
    dateJoined:Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))