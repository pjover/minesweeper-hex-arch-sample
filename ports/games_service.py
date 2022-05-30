from abc import abstractmethod
from typing import Tuple

from domain import domain


class GamesService:

    @abstractmethod
    def get(self, id: str) -> Tuple[domain.Game, domain.Error]:
        pass

    @abstractmethod
    def create(self, name: str, size: int, bombs: int) -> Tuple[domain.Game, domain.Error]:
        pass

    @abstractmethod
    def reveal(self, id: str, row: int, col: int) -> Tuple[domain.Game, domain.Error]:
        pass
