import os
from pathlib import Path

PROJECT_DIRECTORY = Path(__file__).resolve().parents[2]
LOG_FILE = os.path.join(PROJECT_DIRECTORY, "py_log.log")
SOURCE_FOLDER = os.path.join(PROJECT_DIRECTORY, "source_files")

PAYLOAD_VARIATIONS = ["Database backup creation",
                      "Automated log file cleanup",
                      "Server health checks",
                      "User account synchronization",
                      "Automated software updates"]
