from typing import TypeAlias
from dataclasses import dataclass

ConfigValue: TypeAlias = int | str | bool | dict[str, int] | None


@dataclass
class MazeConfig:
    width: int
    height: int
    entry: dict[str, int]
    exit: dict[str, int]
    output_file: str
    perfect: bool
