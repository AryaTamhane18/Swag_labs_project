import os
import logging
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Set up logging directly in this file
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
log = logging.getLogger(__name__)


def load_env():
    """
    Load environment variables from a .env file located at the project's root directory.
    """
    env_path = PROJECT_ROOT / ".env"
    load_dotenv(dotenv_path=env_path)
    log.debug("Environment loaded")


# def get_homepage_url():
#     """
#     Retrieve the homepage URL for Zara from environment variables or provide a default.
#     """
#     return os.getenv("SWAGLABS_HOMEPAGE_URL", "https://www.saucedemo.com/v1/inventory.html")



def get_from_env(name: str, required: bool = True):
    value = os.getenv(name)
    if required and not value:
        raise RuntimeError(f"No {name} environment variable found.")
    return value


def get_window_size():
    window_size = get_from_env("WINDOW_SIZE").split("x")
    if not len(window_size) == 2:
        raise RuntimeError("Invalid window size format in .env file.")
    return int(window_size[0]), int(window_size[1])


def is_truthy(bool_as_string: str):
    return str(bool_as_string).lower() == "true"
