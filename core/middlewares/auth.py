from django.http import HttpRequest
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from core.models.pengguna import Pengguna
from core.repositories.pengguna import PenggunaRepository


class AuthorizationMiddleware(MiddlewareMixin):
    def __call__(self, request: HttpRequest) -> HttpResponse:
        auth_token = request.headers.get('Authorization')
        if auth_token and auth_token.startswith('Bearer '):
            try:
                print('middle')
                print(auth_token)
                username: str = auth_token.split(' ')[1]
                pengguna: Pengguna | None = PenggunaRepository().find_by_username(username=username)
                print(pengguna)
                request.pengguna = pengguna  # type: ignore
            except:
                return self.get_response(request)  # type: ignore

        return self.get_response(request)  # type: ignore
