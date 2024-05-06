from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.pengguna import Pengguna
from core.repositories.pengguna import PenggunaRepository
from core.utils.exceptions.bad_request import BadRequestException
from core.utils.response import Response
from rest_framework import status


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        username: str | None = request.data.get('username', None)
        password: str | None = request.data.get('password', None)

        if not username:
            raise BadRequestException('Username is required.')
        if not password:
            raise BadRequestException('Password is required.')

        pengguna: Pengguna | None = PenggunaRepository().find_by_username(username=username)
        if not pengguna:
            raise BadRequestException('Invalid username.')
        elif password != pengguna.password:
            raise BadRequestException('Wrong password.')

        data_json = {
            'username': pengguna.username
        }

        return Response(message='Login success!', data=data_json, status=status.HTTP_200_OK)


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        ...
