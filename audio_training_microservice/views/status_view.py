from fastapi import APIRouter

import config, dto

router = APIRouter()


@router.get("/status", operation_id="status_view", response_model=dto.StatusViewResponse)
async def status_view() -> dto.JSON:
    """
    Status view returning the name and version of this service and a link to Swagger documentation.

    \f
    :return:
    """

    return dto.StatusViewResponse(
        service="audio_training_microservice",
        version=config.VERSION,
        environment=config.ENVIRONMENT,
        links=[{"href": "/docs", "rel": "documentation", "type": "GET"}]
    )