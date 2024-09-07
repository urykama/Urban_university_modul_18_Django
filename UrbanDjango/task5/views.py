from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister


# Create your views here.
def sign_up_by_html(request):
    users = ['admin', 'Mike', 'Andrei', 'Ildar', 'Marat']
    info = {}
    error = ''
    if request.method == 'POST':
        for key in ('username', 'password', 'password_check', 'age'):
            info[key] = request.POST.get(key, '')

        error = check(info, users)
        if not error:
            return HttpResponse(f'Приветствуем, {info["username"]}')
    return render(request, 'fifth_task/registration_page.html', context={'error': error})


def sign_up_by_django(request):
    users = ['admin', 'Mike', 'Andrei', 'Ildar', 'Marat']
    info = {}
    error = ''
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            for key in ('username', 'password', 'password_check', 'age'):
                info[key] = request.POST.get(key, '')

            error = check(info, users)
            if not error:
                return HttpResponse(f'Приветствуем, {info["username"]}')
        else:
            form = UserRegister()
    return render(request, 'fifth_task/registration_page.html', context={'error': error})


def registration(request):
    return render(request, 'fifth_task/registration_page.html')


def check(info, users):
    if info['password'] != info['password_check']:
        return 'Пароли не совпадают'
    elif int(info['age']) < 18:
        return 'Вы должны быть старше 18'
    elif info['username'] in users:
        return 'Пользователь уже существует'
    return ''
