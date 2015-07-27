"""This module implements the core punter functionality."""


import os
import json
import requests
from . import exceptions


API_ENDPOINT = 'https://api.emailhunter.co/v1/'
EXIST_URL = API_ENDPOINT + 'exist?email={0}&api_key={1}' 
SEARCH_URL = API_ENDPOINT + 'search?domain={0}&api_key={1}' \
            '&offset={2}&type={3}'


class Search(object):
    """A punter search result.

    Search represents the primary result returned from either domain or
    email searches. The data/attributes available are relevant only to 
    the type of search made.

    Usage::

        >>> import punter
        >>> key = 'd08d2ba22218d1b59df239d03fc5e66adfaec2b2'
        >>> s = punter.Search(key)
        >>> s.domain('www.python.org')

    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.status = None
        self.text = ''
        self.count = 0
        self.emails = {}
        self.exist = False

    def domain(self, url, offset=0, type='personal'):
        url = SEARCH_URL.format(url, self.api_key, offset, type)
        resp = requests.get(url)
        return resp.content
        
    def email(self, email):
        pass
