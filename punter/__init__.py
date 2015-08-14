"""punter - A simple wrapper for the Email Hunter API."""


__title = 'punter'
__author__ = 'Joshua Goodlett'
__version__ = '0.1.2'
__license__ = 'MIT'


from .api import search
from .exceptions import (
    PunterException,
    InvalidAPIKeyException,
    InvalidQueryStringException
)
