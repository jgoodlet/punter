"""Essential punter API."""


import json
import requests
from . import exceptions
from .helpers import get_endpoint


def search(api_key, domain='', email='', offset=0, type='personal'):
    """Get a list of emails for the given domain.

    Returns the list of all emails from a given domain. Each email is
    returned with one or more sources, a type (generic or personal)
    and the date it was extracted on.

    :param domain: Domain name from which you want to find emails.
    :param email: The target email to search for.
    :param offset: Specifies the number of emails to skip.
    :param type: Specifies email type (i.e. generic or personal).
    :param api_key: Secret client API key.

    """
    
    url = get_endpoint(api_key, domain, email, offset, type)

    try:
        return requests.get(url).json()
    except requests.exceptions.RequestException as err:
        raise PunterException(err)