from django.shortcuts import render

# Главная страница
def main_page(request):
    return render(request, 'third_task/main.html')

# Магазин
def store_page(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {'games': games}
    return render(request, 'third_task/store.html', context)

# Корзина
def cart_page(request):
    return render(request, 'third_task/cart.html')
