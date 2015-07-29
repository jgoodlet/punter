"""Custom exceptions for the punter package."""


class PunterException(Exception):
    def __init__(self, *args, **kwargs):
        super(PunterException, self).__init__(*args, **kwargs)


class InvalidAPIKeyException(PunterException):
    pass


class InvalidQueryStringException(PunterException):
    pass
