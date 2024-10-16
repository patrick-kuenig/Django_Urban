from django.shortcuts import render


# Create your views here.
def main_page(request):
    return render(request, 'menu.html')


def shop_page(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'Payday2']
    context = {
        'games': games,
    }
    return render(request, 'shop.html', context)


def cart_page(request):
    return render(request, 'cart.html')
