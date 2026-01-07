from sqlalchemy import String
from src.models.base import UUIDModel, TimestampedModel
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column

class User(UUIDModel, TimestampedModel):
    firstName:Mapped[str] = mapped_column(String)
    middleName:Mapped[str] = mapped_column(String, nullable=True)
    lastName:Mapped[str] = mapped_column(String)
    email:Mapped[str] = mapped_column(String,unique=True, index = True)
    phoneNumber:Mapped[str] = mapped_column(String,nullable=True)
    password:Mapped[str] = mapped_column(String)
    role:Mapped[str] = mapped_column(String)
    