from abc import abstractmethod
from typing import Tuple

from core.domain import domain


class GamesRepository:

    @abstractmethod
    def get(self, id: str) -> Tuple[domain.Game, domain.Error]:
        pass

    @abstractmethod
    def save(self, game: domain.Game) -> domain.Error:
        pass
