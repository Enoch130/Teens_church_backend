from typing import Optional
from sqlalchemy import Column,String,Integer,Float,DateTime,ForeignKey
from src.models.base import UUIDModel, TimestampedModel
from uuid import UUID
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.orm import Mapped, mapped_column


class Images(UUIDModel, TimestampedModel):
    __tablenames__ = "Images"
    imageID: Mapped[UUID] = mapped_column(pgUUID(as_uuid=True),primary_key=True,index = True)
    URL: Mapped[str] = mapped_column(String, nullable=False)
    alttext: Mapped[str] = mapped_column(String, nullable=False)
    


