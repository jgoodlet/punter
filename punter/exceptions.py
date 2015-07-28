"""Custom exceptions for the punter package."""


class PunterException(Exception):
    def __init__(self, *args, **kwargs):
        super(PunterException, self).__init__(*args, **kwargs)


class MissingArgumentsException(PunterException):
    pass


class InvalidAPIKeyException(PunterException):
    pass