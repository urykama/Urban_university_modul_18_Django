from django.shortcuts import render


# Create your views here.
def games(requests):
    title = 'Игры'
    dates = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', 'Doom']
    releases = [f'{date}' for i, date in enumerate(dates, start=1)]
    context = {'title': title,
               'releases': releases}

    return render(requests, 'third_task/games.html', context=context)


def cart(requests):
    title = 'Корзина'
    dates = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', 'Doom']
    releases = [f'{date}' for i, date in enumerate(dates, start=1)]
    context = {'title': title,
               'team': releases}

    return render(requests, 'third_task/cart.html', context=context)
