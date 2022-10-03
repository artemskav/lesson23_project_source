class BaseError(Exception):
    message = "Ошибка!"


class SomeError(BaseError):
    message = "Some wrong"