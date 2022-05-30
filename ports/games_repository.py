from abc import abstractmethod
from typing import Tuple

from domain import domain


class GamesRepository:

    @abstractmethod
    def get(self, id: str) -> Tuple[domain.Game, domain.Error]:
        pass
