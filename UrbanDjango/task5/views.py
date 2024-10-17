from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister


# Create your views here.
def sign_up_by_html(request):
    users = ['user', 'Patrick', 'Vlad']
    info = {}
    context = {
        'info': info
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = hash(request.POST.get('password'))
        repeat_password = hash(request.POST.get('repeat_password'))
        age = int(request.POST.get('age'))

        if password == repeat_password and age >= 18 and username not in users:
            users.append(username)
            return HttpResponse(f"Приветствуем, {username}")

        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'

        elif username in users:
            info['error'] = 'Пользователь уже существует'

    if info.get('error') is not None:
        return HttpResponse(info["error"])

    return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    users = ['user', 'Patrick', 'Vlad']
    info = {}
    context = {
        'info': info,
    }
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            password = form.cleaned_data('password')
            repeat_password = form.cleaned_data('repeat_password')
            age = form.cleaned_data('age')
            context['form'] = form

            if password == repeat_password and age >= 18 and username not in users:
                users.append(username)
                return HttpResponse(f"Приветствуем, {username}")

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'

            elif username in users:
                info['error'] = 'Пользователь уже существует'

        if info.get('error') is not None:
            return HttpResponse(info["error"])

    else:
        form = UserRegister()
        context['form'] = form

    return render(request, 'registration_page.html', context)
