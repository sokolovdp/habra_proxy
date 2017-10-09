# -*- coding: utf-8 -*-

import requests

import habra_init
from habra_filter import filter_html_content


class UwsgiRouter:
    def __init__(self, route_table):
        self.route_table = route_table
        self.response_status = "111"
        self.response_headers = [('Content-Type', 'text/html'), ]
        self.response_body = "HABRA-PROXY INITIAL STATE"

    def response(self, status, body):
        self.response_status = status
        self.response_body = body

    def no_method(self):
        self.response_status = "405"
        self.response_body = "INVALID METHOD"

    def router(self, environ, start_response):
        method_route = self.route_table.get(environ['REQUEST_METHOD'], None)
        if method_route:
            method_route(self, path=environ['REQUEST_URI'])
        else:
            self.no_method()
        start_response(self.response_status, self.response_headers)
        return [self.response_body]


def get_method(habra_router, path="/", **kwargs):
    page = requests.get(habra_init.HABRA_URL + path)
    new_html_page = filter_html_content(page.text)
    habra_router.response("200", new_html_page.encode(encoding='utf-8'))


routing_table = {"GET": get_method}
router = UwsgiRouter(routing_table)
application = router.router
