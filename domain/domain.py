from dataclasses import dataclass
from typing import List


@dataclass
class BoardSettings:
    size: int
    bombs: int


@dataclass
class Board:
    cells: List[List[str]]


@dataclass
class Game:
    id: str
    name: str
    state: str
    board_settings: BoardSettings
    Board: Board


@dataclass
class Error:
    message: str
