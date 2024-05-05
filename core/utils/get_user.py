from rest_framework.request import Request

from core.models.pengguna import Pengguna


def get_user(request: Request) -> Pengguna | None:
    try:
        return request.pengguna  # type: ignore
    except:
        return None
