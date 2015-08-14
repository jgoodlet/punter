"""Test suite for the punter library."""


import pytest
import punter.exceptions as exc
from punter.api import search
from punter.helpers import get_query_type, get_endpoint


class TestQueryType(object):

    def test_query_type_email_valid(self):
        emails = [
            'johndoe@gmail.com',
            'john.doe@gmail.com',
            'john-doe007@gmail.com',
            'john+doe007@gmail.com',
        ]

        for email in emails:
            assert get_query_type(email) == 'email'

    def test_query_type_email_malformed(self):
        emails = [
            'johndoe @ gmail.com',
            'john.doe@gmail',
            'john.doe@.com',
            'john@'
            '@', ''
        ]

        for email in emails:
            assert get_query_type(email) == ''

    def test_query_type_domain_valid(self):
        domains = [
            'www.google.com',
            'github.com',
            'github.org',
            'github.edu',
            'github.io',
            'github.me'
        ]

        for domain in domains:
            assert get_query_type(domain) == 'domain'

    def test_query_type_domain_malformed(self):
        domains = [
            '//www.google.com/',
            'https:/github.com/',
            'htt://github.org',
            'githubedu',
            '.io',
            'github.'
        ]

        for domain in domains:
            assert get_query_type(domain) == ''


class TestEndpont(object):

    def test_empty_query(self):
        with pytest.raises(exc.InvalidQueryStringException):
            key = 'd08d2ba22218d1b59df239d03fc5e66adfaec2b2'
            result = get_endpoint(key, '', 0, '')


class TestSearch(object):

    def test_api_key_empty(self):
        with pytest.raises(exc.InvalidAPIKeyException):
            search('', 'www.google.com')

    def test_api_key_invalid_length(self):
        with pytest.raises(exc.InvalidAPIKeyException):
            search('1234567890', 'www.google.com')

    def test_api_key_valid(self):
        key = 'd08d2ba22218d1b59df239d03fc5e66adfaec2b2'
        result = search(key, 'www.google.com')
        assert result is not None 

