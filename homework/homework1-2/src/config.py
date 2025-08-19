from __future__ import annotations
import os
from pathlib import Path
from dotenv import load_dotenv
# Project root = parent of this file's folder (…/homework/homework1)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_PATH = PROJECT_ROOT / ".env"

def load_env() -> None:
    """Load .env from homework/homework1 if present."""
    load_dotenv(ENV_PATH)

def get_key(name: str, default: str | None = None) -> str:
    """Read a key from environment (after load_env)."""
    val = os.getenv(name, default)
    if val is None:
        raise KeyError(f"Missing environment variable: {name}")
    return val

def get_data_dir() -> Path:
    """Return the data directory (from DATA_DIR or default './data')."""
    data_dir = get_key("DATA_DIR", "./data")
    path = (PROJECT_ROOT / data_dir).resolve()
    path.mkdir(parents=True, exist_ok=True)
    return path
