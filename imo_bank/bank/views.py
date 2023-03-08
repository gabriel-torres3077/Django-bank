from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.views import APIView
from bank.models import Account, Transaction
from rest_framework import serializers
from bank.serializer import AccountSerializer, TransactionSerializer
from django.http import Http404
from .models import User
# Create your views here.

class AccountViewSet(APIView):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get(self, request):
        accounts = Account.objects.all()
        serializer = self.serializer_class(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AccountDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        account = self.get_object(pk=pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        order = self.get_object(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TransactionDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Transaction.objects.get(id=pk)
        except Transaction.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        transaction = self.get_object(pk)
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        transaction = self.get_object(pk=pk)
        serializer = TransactionSerializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        order = self.get_object(pk=pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Transfer(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        user = User.objects.get(email=request.user)
        account = Account.objects.get(user=user.id)
        transaction_type = request.data["type"]
        t_amount = float(request.data["amount"])
        print(account.balance)
        if request.data["target"] is not None:
            account.transaction(
                type=transaction_type,
                t_amount=t_amount,
                target=request.data["target"]
            )
        else:
            account.transaction(
                type=transaction_type,
                t_amount=t_amount,
            )
        print(account.balance)

        return Response(status=status.HTTP_200_OK)