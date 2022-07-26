from fastapi import APIRouter

import config, dto
from config import logger

router = APIRouter()


@router.get("/status", operation_id="status_view", response_model=dto.StatusViewResponse)
async def status_view() -> dto.JSON:
    """
    Status view returning the name and version of this service and a link to Swagger documentation.

    \f
    :return:
    """

    print("ramish")
    
    logger.info("Called API to get the status of an application")

    return dto.StatusViewResponse(
        service="audio_training_microservice",
        version=config.VERSION,
        environment=config.ENVIRONMENT,
        links=[{"href": "/docs", "rel": "documentation", "type": "GET"}]
    )