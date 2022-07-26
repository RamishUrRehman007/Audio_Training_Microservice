import inspect
import logging
import re
from typing import Callable

import uvicorn  # type: ignore
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, Response
from fastapi.routing import APIRoute
from pydantic import BaseModel

import config, dto
from error_handler import exception_handler
from exceptions import AudioTrainingMicroserviceAppError
from libs import log_sanitizer
from views import (
    status_view,
    inference_view
)


def init_logging() -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)-5.5s [%(name)s:%(lineno)s][%(threadName)s] %(message)s",
        level=config.LOG_LEVEL,
    )
    log_sanitizer.sanitize_formatters(logging.root.handlers)


def include_routers(app: FastAPI) -> None:
    app.include_router(status_view.router, prefix="/v1")
    app.include_router(inference_view.router, prefix="/v1")



def add_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AudioTrainingMicroserviceAppError, exception_handler)


def add_middlewares(app: FastAPI) -> None:
    @app.middleware("http")
    async def replace_content_type_header(request: Request, call_next: Callable) -> Response:
        response = await call_next(request)
        if response.headers.get("content-type") == "application/json":
            response.headers["content-type"] = "application/json; charset=utf-8"
        return response


init_logging()

app = FastAPI(
    title="audio_training_microservice",
    root_path=config.ROOT_PATH,
    openapi_url="/openapi.json" if config.ENVIRONMENT == "dev" else None,
)

include_routers(app)
add_exception_handlers(app)
add_middlewares(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "HEAD", "PATCH"],
    allow_headers=["*"],
)


@app.get("/")
async def root_view() -> RedirectResponse:
    return RedirectResponse(url=config.ROOT_PATH + "/docs", status_code=303)


if __name__ == "__main__":  # pragma: no cover
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=10000,
        log_level=config.UVICORN_LOG_LEVEL,
        reload=config.ENABLE_RELOAD_UVICORN,
    )
