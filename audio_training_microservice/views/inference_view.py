from typing import Any, List, Iterator, Tuple
from fastapi import HTTPException

from fastapi import APIRouter
from domains import inference_domain
import dto
from config import logger
import os
router = APIRouter()


@router.get("/api/detect/{utterance}/{audio_loc}", response_model=List[dto.Prediction])
def generate_phrase_detections(utterance: str, audio_loc: str) -> Any:
    """Run inference on an audio file with a model for an utterance. Currently
    available utterances are: "call", "is", "recorded"

    Args:
        utterance: Case sensitive name of the model to be used for inference
        audio_loc: The full or relative path to the audio file for which inference
            is to be executed
    """
    try:
        model = inference_domain.MODEL_DICT[utterance]
    except KeyError:
        raise HTTPException(
            404, f"Utterance {utterance} not found in local model dictionary"
        )

    try:
        resampled_audio = inference_domain.load_resampled(audio_loc, inference_domain.SAMPLE_RATE)
    except FileNotFoundError:
        raise HTTPException(404, f"File {audio_loc} not found")

    predictions = []
    for time, audio_snip in inference_domain.iterate_call(resampled_audio):
        confidence = model(audio_snip)
        if confidence > inference_domain.MODEL_CONFIDENCE_THRESHOLD:
            predictions.append(
                dto.Prediction(
                    phrase=utterance, time=time / inference_domain.SAMPLE_RATE, confidence=confidence
                )
            )

    return predictions