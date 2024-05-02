from typing import Any
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc: Exception, context: dict[str, Any]) -> Response:
    return Response(data={
        'message': 'Internal Server Error'
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
