from rest_framework.views import APIView
from rest_framework.request import Request
from core.utils.response import Response


class AllContributorsView(APIView):
    def get(self, request: Request) -> Response:
        ...


class AllSutradaraView(APIView):
    def get(self, request: Request) -> Response:
        ...


class AllPemainView(APIView):
    def get(self, request: Request) -> Response:
        ...


class AllScriptWriterView(APIView):
    def get(self, request: Request) -> Response:
        ...
