from django.shortcuts import render
from django.views import View
from finance.forms import RegisterForm
# Create your views here.
class RegisterView(View):
    def get(self,request,*args, **kwargs):
        form = RegisterForm()
        return render(request,'finance/register.html',{'form':form})
    def post(self,request,*args, **kwargs):
        form = RegisterForm(request.POST)
        return render(request,'finance/register.html',{'form':form})