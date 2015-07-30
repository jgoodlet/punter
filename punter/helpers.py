"""A collection of helper/utility functions."""


import re
from . import exceptions as ex


API_ENDPOINT = 'https://api.emailhunter.co/v1/'
EMAIL_URL = API_ENDPOINT + 'exist?email={0}&api_key={1}'
DOMAIN_URL = (API_ENDPOINT + 'search?domain={0}&api_key={1}'
              '&offset={2}&type={3}')


EMAIL_RE = re.compile(
    '''
    [\w\d.+-]+             # username
    @
    ([\w\d.]+\.)+          # domain name prefix
    (com|org|edu|io|me)    # support more top-level domains
    ''',
    re.UNICODE | re.VERBOSE | re.IGNORECASE)


# From Django, slightly modified (http://bit.ly/1ILBmfL)
URL_RE = re.compile(
    '''
    ^(?:http)s?:// # http:// or https://
    (?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+
    (?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|             # domain...
    localhost|                                      # localhost...
    \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|             # ...or ipv4
    \[?[A-F0-9]*:[A-F0-9:]+\]?)                     # ...or ipv6
    (?::\d+)?                                       # optional port
    (?:/?|[/?]\S+)$
    ''',
    re.VERBOSE | re.IGNORECASE)


def get_query_type(query):
    """Gets the type of query in use (email or url).

    In order to provide a proper API endpoint it is necessary to first
    determine the type of query the client is using. There are only two
    options currently: 1) domain or 2) email.

    :param query: Search query provided by client.

    """

    if URL_RE.match(query):
        query_type = 'domain'
    elif EMAIL_RE.match(query):
        query_type = 'email'
    else:
        query_type = ''

    return query_type


def get_endpoint(api_key, query, offset, type):
    """Return endpoint URL for the relevant search type.

    The base API endpoint only varies by type of search requested, of
    which there are two: 1) domain search and 2) email search. Each
    search type requires different parameters, though api_key is common
    between them.

    Note: if both a url and email address are provided the endpoint
    returned will default to the domain search as it is considered to
    be the primary function of the API and thus takes precedent.

    :param api_key: Secret client API key.
    :param query: URL or email address on which to search.
    :param offset: Specifies the number of emails to skip.
    :param type: Specifies email type (i.e. generic or personal).

    """

    query_type = get_query_type(query)

    if query_type not in ('domain', 'email'):
        raise ex.InvalidQueryStringException('Invalid query string')

    if query_type == 'domain':
        return DOMAIN_URL.format(query, api_key, offset, type)
    else:
        return EMAIL_URL.format(query, api_key)
