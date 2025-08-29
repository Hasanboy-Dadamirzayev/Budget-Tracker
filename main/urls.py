from django.urls import path
from .views import *


urlpatterns = [
    path('tranzit/', TranzitCreateAPIView.as_view()),
]