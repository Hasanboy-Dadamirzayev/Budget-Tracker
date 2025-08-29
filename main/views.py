from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters
from rest_framework.exceptions import ValidationError
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class TranzitCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Tranzit.objects.all()
    serializer_class = TranzitSerializer

    filter_backends = [filters.SearchFilter, OrderingFilter]

    search_fields = ["title", "type"]
    ordering_fields = ["amount", "-amount", "title"]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)



    def perform_create(self, serializer):
        tranzit = serializer.save(user=self.request.user)

        user = self.request.user

        if tranzit.type == 'Income':
            user.balance += tranzit.amount
        elif tranzit.type == 'Expense':
            if user.balance < tranzit.amount:
                raise ValidationError("Balansdan amount katta bolishi mumkin emas!")
            user.balance -= tranzit.amount
        user.save()


