import uuid
from typing import Any

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    Text,
    text,
)
from sqlalchemy.event import listens_for
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from session import AsyncSessionLocal

Base = declarative_base()  # type: Any


async def get_db() -> AsyncSessionLocal:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


def generate_uuid():
    return str(uuid.uuid4())


class AudioFile(Base):
    __tablename__ = "audio_files"

    id = Column(Integer, primary_key=True, index=True)
    audio_file_name = Column(Text)
    audio_file_duration = Column(Integer)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    deleted_at = Column(DateTime(timezone=True))

    model_prediction = relationship("ModelPrediction", back_populates="audio_files", lazy="select")


class ModelPrediction(Base):
    __tablename__ = "model_predictions"

    id = Column(Integer, primary_key=True, index=True)
    audio_file_id = Column(Integer, ForeignKey("audio_files.id"), nullable=False)
    confidence_utterance = Column(Text)
    confidence_time = Column(Integer)
    confidence_confidence = Column(Float)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    deleted_at = Column(DateTime(timezone=True))

    audio_file = relationship("AudioFile", back_populates="model_predictions", lazy="select")
