import adapters.driven.games_repository
import ports.games_service
import services.games_service


def dependency_injection() -> ports.games_service.GamesService:
    _games_repository = adapters.driven.games_repository.GamesRepository()
    _games_service = services.games_service.GamesService(_games_repository)
    return _games_service
