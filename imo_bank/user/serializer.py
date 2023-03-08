from rest_framework import serializers
from . import services


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField()
    cpf = serializers.CharField()
    birth = serializers.CharField()
    gender = serializers.CharField()
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)