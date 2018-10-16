import re

import requests


class URLProvider:
    def __init__(self):
        self.__base = 'http://www.deeplearningbook.org/'
        html = requests.get(self.__base).text
        matchs = re.findall('href="(contents/.*?)"', html)
        self.__urls = []
        for m in matchs:
            self.__urls.append(self.__base + m)

    def next(self):
        for i in self.__urls:
            yield i
