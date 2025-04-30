from django.urls import path
from .views import index, login, registration, catalogue, order, bmw, mercedes, toyota, electric_car


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
    path('catalogue/', catalogue, name='catalogue'),
    path('order/', order, name='order'),
    path('bmw/', bmw, name='bmw'),
    path('mercedes/', mercedes, name='mercedes'),
    path('toyota/', toyota, name='toyota'),
    path('electric_car/', electric_car, name='electric_car'),
]
