from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from .models import Buyer
from .models import Game


# Главная страница
def main_page(request):
    menu_items = [
        {'title': 'Главная', 'url_name': 'main_page'},
        {'title': 'Магазин', 'url_name': 'shop_page'},
        {'title': 'Корзина', 'url_name': 'cart_page'}
    ]
    return render(request, 'first_task/main_page.html', {'menu_items': menu_items})

# Первая доп. страница: Магазин
# def shop_page(request):
#     items = {
#         'item1': 'Товар 1',
#         'item2': 'Товар 2',
#         'item3': 'Товар 3'
#     }
#     return render(request, 'first_task/shop_page.html', {'items': items})
def shop_page(request):
    # Получаем все товары из базы данных
    items = Game.objects.all()
    context = {
        'items': items
    }
    return render(request, 'first_task/shop_page.html', context)

# Вторая доп. страница: Корзина
def cart_page(request):
    context = {
        'games': ['Atomic Heart', 'Cyberpunk 2077']  # Список с играми
    }
    return render(request, 'first_task/cart_page.html', context)

users = ['user1', 'user2', 'user3']


# Создание формы регистрации
class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    age = forms.IntegerField(label='Введите свой возраст')


# def sign_up_by_html(request):
#     info = {}
#
#     if request.method == 'POST':
#         form = UserRegister(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             repeat_password = form.cleaned_data['repeat_password']
#             age = form.cleaned_data['age']
#
#             if username in users:
#                 info['error'] = 'Пользователь уже существует'
#             elif password != repeat_password:
#                 info['error'] = 'Пароли не совпадают'
#             elif age < 18:
#                 info['error'] = 'Вы должны быть старше 18'
#             else:
#                 # Регистрация прошла успешно, редирект на главную страницу
#                 return redirect('main_page')  # Перенаправление на главную страницу
#
#     else:
#         form = UserRegister()  # Инициализация пустой формы
#
#     info['form'] = form  # Передаем форму в контекст
#     print('first_task/registration_page.html')
#     return render(request, 'first_task/registration_page.html', info)
def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверяем, существует ли пользователь с таким именем
            if Buyer.objects.filter(username=username).exists():
                info['error'] = 'Пользователь с таким именем уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                # Создаем нового пользователя
                Buyer.objects.create(username=username, password=password, age=age)
                return redirect('main_page')  # Перенаправление на главную страницу

    else:
        form = UserRegister()  # Инициализация пустой формы

    info['form'] = form  # Передаем форму в контекст
    return render(request, 'first_task/registration_page.html', info)

def sign_up_by_django(request):
    # Аналогично, добавьте логику для этого представления
    return HttpResponse("Это представление для регистрации через Django")
