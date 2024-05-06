from typing import Any
from rest_framework.response import Response
from rest_framework import status

from core.utils.exceptions.bad_request import BadRequestException
from core.utils.exceptions.forbidden import ForbiddenException
from core.utils.exceptions.not_found import NotFoundException
from core.utils.exceptions.unauthorized import UnauthorizedException


def custom_exception_handler(exc: Exception, context: dict[str, Any]) -> Response:
    code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = 'Internal Server Error'

    if isinstance(exc, NotFoundException):
        code = status.HTTP_404_NOT_FOUND
        message = str(exc)
    elif isinstance(exc, ForbiddenException):
        code = status.HTTP_403_FORBIDDEN
        message = str(exc)
    elif isinstance(exc, UnauthorizedException):
        code = status.HTTP_401_UNAUTHORIZED
        message = str(exc)
    elif isinstance(exc, BadRequestException):
        code = status.HTTP_400_BAD_REQUEST
        message = str(exc)

    print(str(exc))

    return Response(data={
        'code': code,
        'success': False,
        'message': message
    }, status=code)
