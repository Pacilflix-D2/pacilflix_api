from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import status
from core.utils.response import Response
from core.repositories.contributors import ContributorRepository


class ContributorsView(APIView):
    def get(self, request: Request):
        contributor_repository = ContributorRepository()
        contributors = contributor_repository.find_all()
        return Response(data=contributors, status=status.HTTP_200_OK, message='Success')
