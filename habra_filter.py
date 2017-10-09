# -*- coding: utf-8 -*-

import re
import bs4
from bs4 import BeautifulSoup, NavigableString
import habra_init

w6 = re.compile(habra_init.PATTERN, re.UNICODE)


def add_trademark(text):
    return re.sub(w6, ur'\1' + habra_init.TRADEMARK, text, re.UNICODE)


def filter_html_content(html_dom):
    soup = BeautifulSoup(html_dom, "html5lib")

    for a_tag in soup.findAll('a', href=True):
        new_href = None
        if habra_init.HABRA_URL in a_tag['href']:
            new_href = a_tag['href'].replace(habra_init.HABRA_URL, habra_init.PROXY_URL)
        elif ('https://' in a_tag['href']) or ('http://' in a_tag['href']):
            new_href = '#'
        else:
            pass
        if new_href:
            a_tag['href'] = new_href

    for div in soup.find_all("div", {"class": "post__text"}):
        for i, element in enumerate(div.contents):
            if isinstance(element, bs4.element.NavigableString) and (len(element) >= habra_init.WORD_LENGTH):
                updated_element = add_trademark(element)
                div.contents[i] = NavigableString(updated_element)

    return unicode(soup)
