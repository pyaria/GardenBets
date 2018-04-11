from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import Round, Board, ScoreBoard
# Create your views here.
class ActiveRound(TemplateView):
    template_name = "show.html"
    def get(self, request, pk):
        r = Round.objects.get(pk=pk)
        return render(request, self.template_name, {'round': r})
    
    def post(self, request):
        pass

    def patch(self, request):
        pass

    def delete(self, request):
        pass

class Games(TemplateView):
    template_name = "index.html"
    def get(self, request):
        rounds = Round.objects.all().filter(active=True)
        return render(request, self.template_name, {'active_rounds': rounds})

class SignIn(TemplateView):
    template_name = "welcome.html"
    signup_form = UserCreationForm

    def get(self, request):
        return render(request, self.template_name, {'signup_form': self.signup_form, "signup": "invisible", "login": "invisible"})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("casino")
        return render(request, self.template_name, {'signup_form': form, 'login': "invisible"})
             