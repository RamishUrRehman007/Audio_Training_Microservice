from typing import List, Optional, Dict, Any

from pydantic import BaseModel


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
