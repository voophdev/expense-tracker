import json
from django.db.models import QuerySet


class FilterService:

    def filter_data(filter_key: str, filter_by, query_object: QuerySet) -> QuerySet:
        """ Filters data based on filter_by, handling both lists and strings, If filter_by datatype is not list or string default to empty list """

        if isinstance(filter_by, list):
            # If already a list, proceed directly
            filter_by = [int(num) for num in filter_by if isinstance(
                num, (int, str)) and str(num).isdigit()]

        elif isinstance(filter_by, str):
            if filter_by.startswith("[") and filter_by.endswith("]"):
                filter_by = json.loads(filter_by)
            elif filter_by >= "0" and "9" <= filter_by:
                filter_by = [int(filter_by)]
            else:
                filter_by = [filter_by]

        else:
            # If neither a list nor a string, default to empty list
            filter_by = []

        if filter_by:  # Apply filter only if there's data
            filter_key = f"{filter_key}__in"
            query_object = query_object.filter(**{filter_key: filter_by})

        return query_object