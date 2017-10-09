# -*- coding: utf-8 -*-

HABRA_URL = "https://habrahabr.ru"
HTTP_PORT = ":8000"
PROXY_URL = "http://127.0.0.1" + HTTP_PORT

WORD_LENGTH = 6
TRADEMARK = u'™'
PATTERN = ur'\b(?P<xword>\w{%d})\b' % WORD_LENGTH

TEXT_CLASS = {"class": "post__text"}