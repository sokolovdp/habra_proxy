# -*- coding: utf-8 -*-

import re
import bs4
from bs4 import BeautifulSoup, NavigableString
import habra_init

w6 = re.compile(habra_init.PATTERN, re.UNICODE)


def add_trademark(text):
    return re.sub(w6, ur'\1' + habra_init.TRADEMARK, text, re.UNICODE)


def replace_tag_content_if_it_is_a_navigable_string(tag, content, position):
    if isinstance(content, bs4.element.NavigableString) and (len(content) >= habra_init.WORD_LENGTH):
        updated_context = add_trademark(content)
        tag.contents[position] = NavigableString(updated_context)


def filter_html_content(html_dom):
    soup = BeautifulSoup(html_dom, "html5lib")

    for a_tag in soup.find_all('a', href=True):
        new_href = None
        if habra_init.HABRA_URL in a_tag['href']:
            new_href = a_tag['href'].replace(habra_init.HABRA_URL, habra_init.PROXY_URL)
        elif ('https://' in a_tag['href']) or ('http://' in a_tag['href']):
            new_href = '#'
        else:
            pass
        if new_href:
            a_tag['href'] = new_href

    for div in soup.find_all("div", attrs=habra_init.TEXT_CLASS):
        for i, element in enumerate(div.contents):
            if element.name == 'p':
                for j, sub_element in enumerate(element.contents):
                    replace_tag_content_if_it_is_a_navigable_string(element, sub_element, j)
            else:
                replace_tag_content_if_it_is_a_navigable_string(div, element, i)

    return unicode(soup)
