import enum
import logging
import os
from typing import List


class LOG_LEV(enum.Enum):
    TRACE = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50


logger = logging.getLogger(__name__)


def _get_boolean_env_variable(name: str) -> bool:
    return os.getenv(name) == "true"


def _get_comma_separated_env_variable(name: str) -> List[str]:
    return [element.strip() for element in os.getenv(name, "").split(",") if element.strip() != ""]

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:8080")
ROOT_PATH = os.getenv("ROOT_PATH", "")
ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
ROOT_USERNAME = os.getenv("ROOT_USERNAME")
ROOT_PASSWORD = os.getenv("ROOT_PASSWORD")
VERSION = "1.0.1"
LOG_LEVEL = int(os.getenv("LOG_LEVEL", logging.NOTSET))
UVICORN_LOG_LEVEL = "info"
ALLOWED_ORIGINS = _get_comma_separated_env_variable("ALLOWED_ORIGINS")

# POSTGRES_URL = os.environ["POSTGRES_URL"]
POSTGRES_URL = os.getenv("POSTGRES_URL", "")
POSTGRES_MAX_POOL_SIZE = int(os.getenv("POSTGRES_MAX_POOL_SIZE", 100))
DEFAULT_LOCALE = "en_US"


ENABLE_RELOAD_UVICORN = _get_boolean_env_variable("ENABLE_RELOAD_UVICORN")

# ====== Feature flags ======
