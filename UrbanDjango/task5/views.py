from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister


# Create your views here.


def sign_up_by_django(request):
    users = ['Mike', 'Andrei', 'Ildar', 'Marat']
    info = {}
    len_info = len(info)
    if request.method == 'POST':
        form = UserRegister(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if form.is_valid():
            if username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif repeat_password != password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', context=info)
            else:
                # username = form.cleaned_data['username']
                # password = form.cleaned_data['password']
                # repeat_password = form.cleaned_data['repeat_password']
                # age = form.cleaned_data['age']
                info = {}
                return render(request, 'fifth_task/registration_page.html',
                              context={'wellcome': f'Приветствуем, {username}!'})
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html')


def sign_up_by_html(request):
    users = ['Mike', 'Andrei', 'Ildar', 'Marat']
    info = {}
    len_info = len(info)
    if request.method == 'POST':
        form = UserRegister(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if form.is_valid():
            if username in users:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif repeat_password != password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'fifth_task/registration_page.html', context=info)
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'fifth_task/registration_page.html', context=info)
            else:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                repeat_password = form.cleaned_data['repeat_password']
                age = form.cleaned_data['age']
                info = {}
                return render(request, 'fifth_task/registration_page.html',
                              context={'wellcome': f'Приветствуем, {username}!'})
    else:
        form = UserRegister()
    return render(request, 'fifth_task/registration_page.html')
