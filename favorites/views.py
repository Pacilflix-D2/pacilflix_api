from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


class FavoriteListView(APIView):
    def get(self, request: Request) -> Response:
        ...

    def delete(self, request: Request) -> Response:
        ...
