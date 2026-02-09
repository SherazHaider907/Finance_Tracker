from django.shortcuts import render, redirect
from django.views import View
from finance.forms import RegisterForm,TransactionForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Transaction
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'finance/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            redirect('dashboard')  
        
class DashboardView(View,LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        return render(request, 'finance/dashboard.html')
    
class TransactionCreateView(View,LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        form = TransactionForm()
        return render(request, 'finance/transactions.html', {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
        return render(request, 'finance/transactions.html', {'form': form})     
    
class TranscationListView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        transaction = Transaction.objects.all()
        return render(request, 'finance/transactions_list.html',{'transaction':transaction})