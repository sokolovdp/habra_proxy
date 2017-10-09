# -*- coding: utf-8 -*-
import re

HABRA_URL = "https://habrahabr.ru"
HTTP_PORT = ":8000"
PROXY_URL = "http://127.0.0.1" + HTTP_PORT

WORD_LENGTH = 6
TRADEMARK = u'™'
PATTERN = ur'\b(?P<xword>\w{%d})\b' % WORD_LENGTH
MATCH = re.compile(PATTERN, re.UNICODE)

TEXT_CLASS = {"class": "post__text"}