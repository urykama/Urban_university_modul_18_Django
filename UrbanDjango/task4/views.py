from django.shortcuts import render


# Create your views here.
def games(requests):
    title = 'Игры'
    # dates = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', 'Doom']
    # releases = [f'{date}' for i, date in enumerate(dates, start=1)]
    dates = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2", "Doom"]}
    releases = [f'{date}' for date in dates['games']]
    context = {'title': title,
               'releases': releases}

    return render(requests, 'fourth_task/games.html', context=context)


def cart(requests):
    title = 'Корзина'
    dates = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2", "Doom"]}
    releases = [f'{date}' for date in dates['games']]
    context = {'title': title,
               'team': releases}

    return render(requests, 'fourth_task/cart.html', context=context)
