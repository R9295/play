from django.contrib.auth.views import logout
from django.shortcuts import render, redirect

from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('auth:index')
