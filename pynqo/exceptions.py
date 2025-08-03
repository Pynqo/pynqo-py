class PynqoError(Exception):
    pass

class AuthenticationError(PynqoError):
    pass

class NotFoundError(PynqoError):
    pass

class BadRequestError(PynqoError):
    pass

class InternalServerError(PynqoError):
    pass