from django.shortcuts import render, redirect
from django.views import View
from finance.forms import RegisterForm
from django.contrib.auth import login

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'finance/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            return redirect('home')  
        return render(request, 'finance/register.html', {'form': form})
