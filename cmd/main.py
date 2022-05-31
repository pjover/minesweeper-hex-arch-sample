from adapters.drivers import http_handler
from di import dependency_injection

if __name__ == '__main__':
    _games_service = dependency_injection.dependency_injection()
    _handler = http_handler.HttpHandler(_games_service)
    _handler.run()
