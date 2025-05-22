from rest_framework import status

def check_status_range(status_code: int, range: list[int] = [ 400, 599 ], message: str = "Unknown HTTP Code"):
    if not ((status_code >= range[0]) and (status_code <= range[1])):
        raise Exception(message)

class ErrorMessage:
    def __init__(self, message: str, status_code: int, details: str | list | dict | int | float | None = None):
        self.__message = message
        self.__status_code = status_code
        self.__details = details
    
    @property
    def message(self) -> str:
        return self.__message
    
    @property
    def status_code(self) -> int:
        return self.__status_code
    
    @property
    def details(self) -> str | list | dict | int | float | None:
        return self.__details
    
    def _error_range(self, error_range: list[int] = [ 400, 599 ], message: str = "Unknown Error"):
        check_status_range(
            status_code=self.status_code,
            range=error_range,
            message=message
        )
    
    def to_json(self) -> dict:
        json = {
            "message": self.message
        }

        if self.details != None:
            json["details"] = self.details

        return json 

class ClientError(ErrorMessage):
    def __init__(self, message: str = "Client Error", status_code: int = status.HTTP_400_BAD_REQUEST, details: str | list | dict | int | float | None = None):
        super().__init__(message, status_code, details)
        self._error_range(
            error_range=[ 400, 499 ],
            message="Client errors are range from 400 to 499."
        )

class InternalError(ErrorMessage):
    def __init__(self, message: str = "Internal Error", status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR, details: str | list | dict | int | float | None = None):
        super().__init__(message, status_code, details)
        self._error_range(
            error_range=[ 500, 599 ],
            message="Internal errors are range from 500 to 599."
        )


class BadRequest(ClientError):
    def __init__(self, message: str = "Bad Request", details: str | list | dict | int | float | None = None):
        super().__init__(message, status_code=status.HTTP_400_BAD_REQUEST, details=details)

class Unauthorized(ClientError):
    def __init__(self, message: str = "Unauthorized", details: str | list | dict | int | float | None = None):
        super().__init__(message, status_code=status.HTTP_401_UNAUTHORIZED, details=details)

class Forbidden(ClientError):
    def __init__(self, message: str = "Forbidden", details: str | list | dict | int | float | None = None):
        super().__init__(message, status_code=status.HTTP_403_FORBIDDEN, details=details)

class NotFound(ClientError):
    def __init__(self, message: str = "Not Found", details: str | list | dict | int | float | None = None):
        super().__init__(message, status_code=status.HTTP_404_NOT_FOUND, details=details)

class TooManyRequests(ClientError):
    def __init__(self, message: str = "Too Many Requests", details: str | list | dict | int | float | None = None):
        super().__init__(message, status_code=status.HTTP_429_TOO_MANY_REQUESTS, details=details)


class InvalidFormBody(BadRequest):
    def __init__(self, details: str | list | dict | int | float | None = None):
        super().__init__("Invalid Form Body", details)

class NoDataFound(NotFound):
    def __init__(self, details: str | list | dict | int | float | None = None):
        super().__init__("No Data Found", details)
