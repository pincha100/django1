from django.contrib import admin
from django.urls import path, include
from task4 import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка
    path('task2/', include('task2.urls')),  # Маршруты для приложения task2
    path('', views.main_page, name='home'),  # Главная страница (корневой URL)
    path('platform/', views.main_page, name='main'),  # Главная страница (повторно)
    path('platform/store/', views.store_page, name='store'),  # Магазин
    path('platform/cart/', views.cart_page, name='cart'),  # Корзина
]
