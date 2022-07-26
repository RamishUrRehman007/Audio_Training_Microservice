from typing import List, Optional, Dict, Any, NewType
from datetime import datetime

from pydantic import BaseModel


AudioFileID = NewType("AudioFileID", int)
ModelPredictionID = NewType("ModelPredictionID", int)


JSON = Dict[str, Any]


class LinkResponse(BaseModel):
    href: str
    rel: str
    type: str


class StatusViewResponse(BaseModel):
    service: str
    version: str
    environment: str
    links: Optional[List[LinkResponse]]


class Prediction(BaseModel):
    phrase: str
    time: int
    confidence: float


class AudioFile(BaseModel):
    id: AudioFileID
    audio_file_name: str
    audio_file_duration: int
    created_at: datetime
    updated_at: datetime


class ModelPrediction(BaseModel):
    id: ModelPredictionID
    audio_file_id: AudioFileID
    confidence_utterance: str
    confidence_time: int
    confidence_confidence: float
    created_at: datetime
    updated_at: datetime