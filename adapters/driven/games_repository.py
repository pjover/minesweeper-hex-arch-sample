from typing import Tuple

from core.domain import domain


class GamesRepository:

    def get(self, id: str) -> Tuple[domain.Game, domain.Error]:
        # TODO Load the game from repo
        return domain.Game(id), domain.success()

    def save(self, game: domain.Game) -> domain.Error:
        # TODO Save the game
        return domain.success()
