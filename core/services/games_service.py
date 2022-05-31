import string
from random import random
from typing import Tuple

from core.domain import domain

from core.ports import games_service, games_repository

class GamesService(games_service.GamesService):

    def __init__(self, games_repository: games_repository.GamesRepository):
        self._games_repository = games_repository

    def get(self, id: str) -> Tuple[domain.Game, domain.Error]:
        return domain.Game(id), domain.success()

    def create(self, name: str, size: int, bombs: int) -> Tuple[domain.Game, domain.Error]:
        if bombs >= size*size:
            return domain.Game(), domain.Error("the number of bombs is invalid")

        _game = domain.Game(self._get_random_id(), name, size, bombs)

        _err = self._games_repository.save(_game)
        if _err.is_error():
            return domain.Game(), domain.Error(f"error saving game into repository: {_err.message}")

        return _game, domain.success()

    @staticmethod
    def _get_random_id():
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))

    def reveal(self, id: str, row: int, col: int) -> Tuple[domain.Game, domain.Error]:
        pass
