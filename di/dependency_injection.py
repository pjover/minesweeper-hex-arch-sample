import adapters.driven.games_repository
import core.services.games_service


def dependency_injection() -> core.ports.games_service.GamesService:
    _games_repository = adapters.driven.games_repository.GamesRepository()
    _games_service = core.services.games_service.GamesService(_games_repository)
    return _games_service
