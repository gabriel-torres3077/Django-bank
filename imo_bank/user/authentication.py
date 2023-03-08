from django.conf import settings
from rest_framework import authentication, exceptions
import jwt

from . import models


class AuthBack(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return None

        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
        except:
            raise exceptions.AuthenticationFailed("Unauthorized")

        user = models.User.objects.filter(id=payload["id"]).first()

        return (user, None)
"""


from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class AuthBack(BaseBackend):
    model = get_user_model()
    def authenticate(self, request = None, email=None, password=None):
        try:
            user = self.model.objects.get(email=email)
        except self.model.DoesNotExist:
            return None
        if self.model.check_password(password) and user is not None:
            return user

    def get_user(self, user_id):
        try:
            return self.model.objects.get(pk=user_id)
        except self.model.DoesNotExist:
            return None

"""