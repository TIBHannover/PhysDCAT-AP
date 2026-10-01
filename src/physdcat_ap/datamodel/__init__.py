"""Data model package for PhysDCAT-AP."""

from pathlib import Path
from .physdcat_ap import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "physdcat_ap.yaml"
