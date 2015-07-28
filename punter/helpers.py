"""A collection of helper/utility functions."""


from . import exceptions


API_ENDPOINT = 'https://api.emailhunter.co/v1/'
EMAIL_URL = API_ENDPOINT + 'exist?email={0}&api_key={1}' 
DOMAIN_URL = (API_ENDPOINT + 'search?domain={0}&api_key={1}'
            '&offset={2}&type={3}')


def get_endpoint(api_key, url, email, offset, type):
    """Return endpoint URL for the relevant search type.

    The base API endpoint only varies by type of search requested, of
    which there are two: 1) domain search and 2) email search. Each 
    search type requires different parameters, though api_key is common
    between them.

    Note: if both a url and email address are provided the endpoint 
    returned will default to the domain search as it is considered to
    be the primary function of the API and thus takes precedent.

    :param api_key: Secret client API key.
    :param url: Domain name from which you want to find emails.
    :param email: The target email to search for.
    :param offset: Specifies the number of emails to skip.
    :param type: Specifies email type (i.e. generic or personal).

    """

    if not api_key or len(api_key) < 40:
        raise InvalidAPIKeyException('Invalid API key.')

    if not url and not email:
        raise MissingArgumentsException('Provide email or url.')

    if url:
        return DOMAIN_URL.format(url, api_key, offset, type)
    else:
        return EMAIL_URL.format(email, api_key)