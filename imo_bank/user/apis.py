
from rest_framework import views, response, exceptions, permissions
from . import serializer as user_serializer
from . import services, authentication
from .models import User
from bank.models import Account
from uuid import uuid4
import datetime

class RegisterApi(views.APIView):
    def post(self, request):
        if User.objects.filter(cpf=request.data["cpf"]).exists():
            return response.Response({"error": "CPF já cadastrado"})
        if User.objects.filter(cpf=request.data["email"]).exists():
            return response.Response({"error": "Email já cadastrado"})
            
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)
        print(serializer.data)
        
        accID = str(uuid4().int) # Gerar número aleatório para a conta bancária
        user = User.objects.get(id=serializer.data["id"])
        account = Account.objects.create(
            account_no = int(accID[:4] + str(serializer.data["id"])),
            user = user,
            balance = 0.0,
            initial_deposit_date = datetime.date.today()
        )

        return response.Response(data=serializer.data)


class LoginApi(views.APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = services.user_email_selector(email=email)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        
        #generate access token
        token = services.create_token(user_id=user.id)

        resp = response.Response()

        resp.set_cookie(key="jwt", value=token, httponly=True)

        return resp


class UserApi(views.APIView):
    """
    This endpoint can only be used
    if the user is authenticated
    """

    authentication_classes = (authentication.AuthBack,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user

        serializer = user_serializer.UserSerializer(user)

        return response.Response(serializer.data)


class LogoutApi(views.APIView):
    authentication_classes = (authentication.AuthBack,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "so long farewell"}

        return resp
    
class DeleteAPI(views.APIView):
    authentication_classes = (authentication.AuthBack,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        email=request.data["email"]
        user = User.objects.get(email=email)
        user.delete()

        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "Usuário excluído"}
        
        return resp