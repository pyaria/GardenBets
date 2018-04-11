from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

# Create your views here.

class Games(TemplateView):
    template_name = "index.html"
    def get(self, request):
        data = {}
        data["user"] = request.user
        return render(request, self.template_name, data)

class SignIn(TemplateView):
    template_name = "welcome.html"
    form = UserCreationForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        import ipdb
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            ipdb.set_trace()
            user = authenticate(username=form.instance.username, password=form.instance.password)
            login(request, user)
            return redirect("casino")
        else:
            ipdb.set_trace()
            try:
                User.objects.get(username=form.instance.username)
                user = authenticate(username=form.instance.username, password=form.instance.password)
                login(request, user)
                return redirect("casino")
            except ObjectDoesNotExist:
                return render(request, self.template_name, {'form': form})
             