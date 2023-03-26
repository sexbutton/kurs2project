from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AuthForm
from django.contrib.auth.views import LoginView, LogoutView

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
