from datetime import datetime

from rest_framework.views import APIView
from rest_framework.request import Request
from core.models.pengguna import Pengguna
from core.repositories.transaksi import TransaksiRepository
from core.utils.response import Response
from rest_framework import status
from core.utils.get_user import get_user
from core.utils.exceptions.unauthorized import UnauthorizedException
from core.models.transaksi import Transaksi


class ActiveSubscriptionView(APIView):
    def get(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login first.')

        transaksi_repository = TransaksiRepository()
        active_subscription = transaksi_repository.get_active_subscription(username=user.username)

        return Response(message='Success get active subscription!', data=active_subscription, status=status.HTTP_200_OK)


class GetTransactionHistory(APIView):
    def get(self, request: Request) -> Response:
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login first.')

        transaksi_repository = TransaksiRepository()
        transaction_history = transaksi_repository.find_by_username(username=user.username)

        return Response(message='Success get transaction history!', data=transaction_history, status=status.HTTP_200_OK)


class InsertTransaction(APIView):
    def post(self, request: Request):
        user: Pengguna | None = get_user(request=request)

        if not user:
            raise UnauthorizedException('Must login first.')

        name = request.data.get('packageName')
        if (name == 'Paket Basic'):
            name = 'Basic'
        elif (name == 'Paket Standard'):
            name = 'Standard'
        else:
            name = 'Premium'

        start = request.data.get('startDate')
        end = request.data.get('endDate')
        metode = request.data.get('paymentMethod')
        tglpembayaran = request.data.get('paymentDate')
        total = request.data.get('totalPayment')
        new_transaction = Transaksi(
            username=user.username,
            name=name,
            start=str(datetime.strptime(start, '%Y-%m-%d')),
            end=str(datetime.strptime(end, '%Y-%m-%d')),
            metode=metode,
            tglpembayaran=str(datetime.strptime(tglpembayaran, '%Y-%m-%d')),
            total=total
        )

        transaksi_repository = TransaksiRepository()
        try:
            transaksi_repository.insert_data(new_transaction)
            return Response("Transaction inserted successfully", status=status.HTTP_201_CREATED)
        except Exception as e:
            raise Exception(e)
