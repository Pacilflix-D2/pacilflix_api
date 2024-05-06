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
        username: str | None = request.data.get('username', None)
        password: str | None = request.data.get('password', None)
        negara_asal: str | None = request.data.get('negara_asal', None)

        if not username:
            raise BadRequestException('Username is required.')
        if not password:
            raise BadRequestException('Password is required.')
        if not negara_asal:
            raise BadRequestException('Negara Asal is required.')

        if len(username) > 50:
            raise BadRequestException('Username is too long.')
        if len(password) > 50:
            raise BadRequestException('Password is too long.')
        if len(negara_asal) > 50:
            raise BadRequestException('Negara Asal is too long.')

        new_user: Pengguna = PenggunaRepository().create(username=username,
                                                         password=password, negara_asal=negara_asal)

        data_json = {
            'username': new_user.username
        }

        return Response(message='Register success!', data=data_json, status=status.HTTP_201_CREATED)
