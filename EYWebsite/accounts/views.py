from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from.forms import LoginForm,RegisterForm
from django.contrib.auth.views import LoginView
# Create your views here.
def signup(request):
    if request.method=='POST':
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
        return redirect('/accounts/signup')
    else:
        form = RegisterForm()
    return render(request,'signup.html',{'form':form})
class Login(LoginView):
    template_name='login.html'
    login_url='/'


    