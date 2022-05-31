from urllib.parse import urlparse

import ports
import http.server
import socketserver

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

PORT = 8080


class HttpHandler(BaseHTTPRequestHandler):
    def __init__(self, games_service: ports.games_service.GamesService):
        self._games_service = games_service

    def run(self):
        logging.basicConfig(level=logging.INFO)
        httpd = HTTPServer(('', PORT), self)
        logging.info('Starting httpd...\n')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        httpd.server_close()
        logging.info('Stopping httpd...\n')

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        _id = query_components["id"]

        _game, err = self._games_service.get(_id)
        # TODO Process game response

        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        query_components = dict(qc.split("=") for qc in query.split("&"))
        _name = query_components["name"]
        _size = int(query_components["size"])
        _bombs = int(query_components["bombs"])

        _game, err = self._games_service.create(_name, _size, _bombs)
        # TODO Process game response

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
