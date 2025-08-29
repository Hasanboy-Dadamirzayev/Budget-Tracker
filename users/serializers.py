from rest_framework.serializers import ModelSerializer
from .models import *

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "balance", "date_joined"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "balance", "date_joined"]