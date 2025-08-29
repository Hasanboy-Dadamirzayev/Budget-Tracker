from rest_framework.serializers import ModelSerializer
from .models import *

class TranzitSerializer(ModelSerializer):
    class Meta:
        model = Tranzit
        fields = "__all__"

        extra_kwargs = {
            "user": {
                "read_only": True
            }
        }