from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

def authorization(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    if user.is_superuser:
                        return HttpResponse('Ошибка! учетная запись административная!')
                    else:
                        login(request, user)
                        return HttpResponse("Вы успешно вошли в систему")
                else:
                    return HttpResponse("Учетная запись неактивна!")
            else:
                return HttpResponse("Проверьте правильность логина и пароля!")

    auth_form = AuthForm()

    return render(request, 'authorization/Login.html', {'form': auth_form})

class LoginView(LoginView):
    template_name = 'authorization/Login.html'

class LogoutView(LogoutView):
    next_page = '/'

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm
        return render(request, 'authorization/registration.html', {"form": form})
