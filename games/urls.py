from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import SignIn, Games

urlpatterns = [
    path('', SignIn.as_view()),
    path('login/', auth_views.login, name="login"),
    path('GreenhouseCasino/', Games.as_view(), name="casino")
]