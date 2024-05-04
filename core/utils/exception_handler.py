from typing import Any
from rest_framework.response import Response
from rest_framework import status

from core.utils.exceptions.not_found import NotFoundException


def custom_exception_handler(exc: Exception, context: dict[str, Any]) -> Response:
    code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'Internal Server Error'

    if isinstance(exc, NotFoundException):
        code = status.HTTP_404_NOT_FOUND
        message = str(exc)

    return Response(data={
        'code': code,
        'success': False,
        'message': message
    }, status=code)
