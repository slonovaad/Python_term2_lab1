from typing import Any
from src.sources.file_source import FileSource
from src.sources.generator_source import GeneratorSource
from src.sources.stdin_source import StdinSource

SOURCE_TYPES: dict[str, Any] = {"file": FileSource,
                                "generator": GeneratorSource,
                                "stdin": StdinSource}
