from rest_framework.request import Request
from rest_framework import status
from typing import List, Dict, Tuple, Optional
from datetime import datetime

class RequestValidatorService:
    """A reusable request validator that checks for missing required fields."""

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Rather not say', 'Rather not say'),
    ]

    def __init__(self, required_fields: Optional[List[str]] = None):
        self.required_fields = required_fields if required_fields is not None else []

    def validate(self, request: Request) -> Optional[Tuple[Dict[str, str], int]]:
        """Validates request data against required fields.

        Args:
            request (Request): The incoming request object.

        Returns:
            Optional[Tuple[Dict[str, str], int]]: Error response if validation fails, otherwise None.
        """
        missing_fields = [
            field for field in self.required_fields if not request.data.get(field)]

        if missing_fields:
            return f"Missing fields: {', '.join(missing_fields)}", status.HTTP_400_BAD_REQUEST

        return None  # No validation errors

    def validate_gender(self, request: Request) -> Optional[Tuple[Dict[str, str], int]]:
        """Validates the gender field in the request.

        Args:
            request (Request): The incoming request object.

        Returns:
            Optional[Tuple[Dict[str, str], int]]: Error response if validation fails, otherwise None.
        """
        # Extract valid choices
        valid_genders = [choice[0] for choice in self.GENDER_CHOICES]

        # Get the gender value from the request
        gender = request.data.get('gender')

        # Validate the gender value
        if gender and gender not in valid_genders:
            return {
                "error": f"Invalid gender value. Valid options are: {', '.join(valid_genders)}"
            }, status.HTTP_400_BAD_REQUEST

        return None  # No validation errors

    def validate_email(self, request: Request) -> Optional[Tuple[Dict[str, str], int]]:
        """Validates the email field in the request.

        Args:
            request (Request): The incoming request object.

        Returns:
            Optional[Tuple[Dict[str, str], int]]: Error response if validation fails, otherwise None.
        """
        email = request.data.get('email')

        # Basic email validation
        if email and '@' not in email:
            return {"error": "Invalid email format."}, status.HTTP_400_BAD_REQUEST

        return None

    def validate_date_params(self, request: Request) -> tuple:
        
        def is_date_valid(date: str, format="%Y-%m-%d"):
            try:
                datetime.strptime(date, format)
                return True
            except ValueError:
                return False
            
        """Validate and parse 'from_date' and 'to_date' query parameters."""
        from_date = request.query_params.get("from_date")
        to_date = request.query_params.get("to_date")

        if not from_date or not to_date:
            raise ValueError(
                "The 'from_date' and 'to_date' query parameters are required.")

        if not (is_date_valid(from_date) and is_date_valid(to_date)):
            raise ValueError(
                "The value of 'from_date' or 'to_date' query parameters is not valid.")

        return from_date, to_date