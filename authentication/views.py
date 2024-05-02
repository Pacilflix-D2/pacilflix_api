from rest_framework.views import APIView
from rest_framework.request import Request

from authentication.transports import LoginResponse, RegisterResponse
from core.utils.response import Response


class LoginView(APIView):
    def post(self, request: Request) -> Response[LoginResponse]:
        ...


class RegisterView(APIView):
    def post(self, request: Request) -> Response[RegisterResponse]:
        ...
