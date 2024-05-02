from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        ...


class RegisterView(APIView):
    def post(self, request: Request) -> Response:
        ...
