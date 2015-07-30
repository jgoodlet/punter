"""Test suite for the punter library."""


from punter.api import search
from punter.helpers import get_query_type, get_endpoint


class TestQueryType:

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