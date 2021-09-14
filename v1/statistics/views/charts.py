from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, serializers

from datetime import timedelta
from django.utils import timezone

from ..models.transactions import Transaction
from ..serializers.charts import ChartSerializer


class TreasuryChartViewSet(viewsets.GenericViewSet):
    '''
    Data up to number of days ago (eg. 1,14,30,max)
    '''

    serializer_class = ChartSerializer

    def create(self, request, format=None):

        serializer = ChartSerializer(data=request.data)

        if serializer.is_valid():

            days = serializer.data['days']

            if days == "max":
                transactions = Transaction.objects.filter(transaction_type=Transaction.TREASURY)

            else:
                try:
                    days = int(days)
                except ValueError:
                    error = {"error": "Invalid day format!!"}
                    raise serializers.ValidationError(error)

                transactions = Transaction.objects.filter(transaction_type=Transaction.TREASURY,
                                                          txs_sent_at__gt=timezone.now() - timedelta(days=days))

            temp = []
            data = []

            for txs in transactions:
                temp.append(txs.amount)
                temp.append(txs.txs_sent_at)
                data.append(temp)
                temp = []

            data = {
                "count": transactions.count(),
                "data": data
            }

            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GovernmentChartViewSet(viewsets.GenericViewSet):
    '''
    Data up to number of days ago (eg. 1,14,30,max)
    '''

    serializer_class = ChartSerializer

    def create(self, request, format=None):

        serializer = ChartSerializer(data=request.data)

        if serializer.is_valid():

            days = serializer.data['days']

            if days == "max":
                transactions = Transaction.objects.filter(transaction_type=Transaction.GOVERNMENT)
            else:
                try:
                    days = int(days)
                except ValueError:
                    error = {"error": "Invalid day format!!"}
                    raise serializers.ValidationError(error)

                transactions = Transaction.objects.filter(transaction_type=Transaction.GOVERNMENT,
                                                          txs_sent_at__gt=timezone.now() - timedelta(days=days))

            temp = []
            data = []

            for txs in transactions:
                temp.append(txs.amount)
                temp.append(txs.txs_sent_at)
                data.append(temp)
                temp = []

            data = {
                "count": transactions.count(),
                "data": data
            }

            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomepageChartViewSet(viewsets.GenericViewSet):
    '''
    Data up to number of days ago (eg. 1,14,30,max)
    '''

    serializer_class = ChartSerializer

    def create(self, request, format=None):

        serializer = ChartSerializer(data=request.data)

        if serializer.is_valid():

            days = serializer.data['days']

            if days == "max":
                transactions = Transaction.objects.all()

            else:

                try:
                    days = int(days)
                except ValueError:
                    error = {"error": "Invalid day format!!"}
                    raise serializers.ValidationError(error)

                transactions = Transaction.objects.filter(txs_sent_at__gt=timezone.now() - timedelta(days=days))

            temp = []
            data = []

            for txs in transactions:
                temp.append(txs.amount)
                temp.append(txs.txs_sent_at)
                data.append(temp)
                temp = []

            data = {
                "count": transactions.count(),
                "data": data
            }

            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
