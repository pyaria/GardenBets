from django.urls import path
from .views import SignIn, Games

urlpatterns = [
    path('', SignIn.as_view()),
    path('GreenhouseCasino', Games.as_view(), name="casino")
]