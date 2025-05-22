from myproject.utils.response_service_util import InternalError, NotFound, BadRequest
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
from django.utils import timezone

class ResponseService:

    def client_response(self, status_code: int, response_data: any = None) -> Response:

        if response_data == None:
            return Response(status=status_code)

        return Response(response_data, status=status_code)


    def ok_response(self, response_data: any) -> Response:
        """Returns 200 status code."""

        return self.client_response(
            status_code=status.HTTP_200_OK,
            response_data=response_data
        )


    def created_response(self, response_data: any) -> Response:
        """Returns 201 status code."""
        return self.client_response(
            status_code=status.HTTP_201_CREATED,
            response_data=response_data
        )


    def no_content_response(self, ) -> Response:
        return self.client_response(
            status_code=status.HTTP_204_NO_CONTENT
        )


    def internal_error_response(self, exception: Exception,
                                error_message: str | None = None, error_details: list[any] | None = None) -> Response:
        """Returns 500 status code."""

        res_error_details = []

        if error_details != None:
            for detail in error_details:
                res_error_details.append(detail)
        res_error_details.append(str(exception))

        error_message = error_message if error_message != None else "Internal Error"
        error_message_obj = InternalError(
            message=error_message, details=res_error_details)

        return self.client_response(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            response_data=error_message_obj.to_json()
        )


    def not_found_response(self, error_details: list[any], error_message: str | None = None) -> Response:
        """Returns 404 status code."""

        error_message = error_message if error_message != None else "Not Found"
        error_message_obj = NotFound(message=error_message, details=error_details)

        return self.client_response(
            status_code=status.HTTP_404_NOT_FOUND,
            response_data=error_message_obj.to_json()
        )


    def bad_request_response(self, error_details: list[any], error_message: str | None = None) -> Response:
        """Returns 400 status code."""

        error_message = error_message if error_message != None else "Bad Request"
        print("BAD REQUEST BEFORE")
        error_message_obj = BadRequest(
            message=error_message, details=error_details)
        return self.client_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            response_data=error_message_obj.to_json()
        ) 