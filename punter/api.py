"""Essential punter API."""

from . import core

def domain(url, api_key, offset=0, type='personal'):
    """Get a list of emails for the given domain.

    Returns the list of all emails from a given domain. Each email is
    returned with one or more sources, a type (generic or personal)
    and the date it was extracted on.

    :param domain: Domain name from which you want to find emails.
    :param offset: Specifies the number of emails to skip.
    :param type: Specifies email type (i.e. generic or personal).
    :param api_key: Secret client API key.

    """
    
    search = core.Search(api_key)
    result = search.domain(url, offset, type)
    return result 


def exist(email, api_key):
    """Determine if a given email exists. Period.

    Executes a search to determine if the given email can be found.
    If the email exists a collection of relevant source data is returned
    to the client (i.e. associated domain, date of extraction, etc..).

    :param email: The target email to search for.
    :param api_key: Secret client API key.

    """
    
    search = core.Search(api_key)
    result = search.email(email)
    return result