"""Essential punter API."""


import json
import requests
from .exceptions import PunterException, InvalidAPIKeyException
from .helpers import get_endpoint


def search(api_key, query, offset=0, type='personal'):
    """Get a list of email addresses for the provided domain.

    The type of search executed will vary depending on the query provided.
    Currently this query is restricted to either domain searches, in which
    the email addresses (and other bits) for the domain are returned, or
    searches for an email address. The latter is primary meant for checking
    if an email address exists, although various other useful bits are also
    provided (for example, the domain where the address was found).

    :param api_key: Secret client API key.
    :param query: URL or email address on which to search.
    :param offset: Specifies the number of emails to skip.
    :param type: Specifies email type (i.e. generic or personal).

    """

    if not isinstance(api_key, str):
        raise InvalidAPIKeyException('API key must be a string')

    if not api_key or len(api_key) < 40:
        raise InvalidAPIKeyException('Invalid API key.')

    url = get_endpoint(api_key, query, offset, type)

    try:
        return requests.get(url).json()
    except requests.exceptions.RequestException as err:
        raise PunterException(err)
