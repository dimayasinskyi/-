import os
from pathlib import Path
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from django.template import Engine
from django.template.loader import get_template
from django.http import HttpResponse
from django.urls import path, reverse
from django.contrib.staticfiles.handlers import StaticFilesHandler


def index(request):
    context = {'title': 'Головна', 'banner': True}
    return HttpResponse(get_template("shop/index.html").render(context, request))


def login(request):
    context = {'title': 'Вхід'}
    return HttpResponse(get_template("shop/login.html").render(context, request))


def registration(request):
    context = {'title': 'Реєстрація'}
    return HttpResponse(get_template("shop/registration.html").render(context, request))


def catalogue(request):
    context = {
        'title': 'Категорії',
        'cars': [
            {
                'image': '/static/img/catalogue/BMW_M5_(G90)_Auto_Zuerich_2024_DSC_6121.jpg',
                'name': 'BMW',
                'description': """BMW — один з найбільш відомих та престижних брендів автомобілів у світі. Відомі своїми спортивними
            характеристиками, розкішним дизайном та передовими технологіями, машини цієї марки підходять для людей, які
            шукають більше ніж просто транспортний засіб.""",
                'url': reverse('bmw')
            },
            {
                'image': '/static/img/catalogue/Mercedes-Benz_W206_IMG_6380.jpg',
                'name': 'Mercedes',
                'description': """Mercedes-Benz — це один із найбільш престижних та відомих брендів у світі автомобілів. Відомий своєю
            неперевершеною якістю, технологіями та розкішшю, Mercedes-Benz поєднує високий рівень комфорту з
            передовими
            технічними інноваціями. Цей бренд ідеально підходить для тих, хто шукає автомобіль преміум-класу з
            елегантним
            дизайном.""",
                'url': reverse('mercedes')
            },
            {
                'image': '/static/img/catalogue/toyota-c-hr__2948279-640x480x70.jpg',
                'name': 'Toyota',
                'description': """Toyota — одна з найбільших і найбільш відомих автомобільних марок у світі, що спеціалізується на
            виробництві
            надійних, економічних і екологічно чистих автомобілів. Toyota пропонує широкий вибір машин від
            компактних
            міських автомобілів до потужних позашляховиків, що поєднують практичність, ефективність і довговічність.""",
                'url': reverse('toyota')
            },
            {
                'image': '/static/img/catalogue/skolko-budut-stoit-elektricheskie-avtomobili-posle-otmeny-rastamozhki__232609-620x0.jpg',
                'name': 'Електричні машини',
                'description': """Електричні машини повністю працюють на електричній енергії, зберігаючи її в акумуляторах. Вони не мають
            викидів CO2 та інших шкідливих газів під час руху, тому вони є найекологічнішим варіантом серед автомобілів.""",
             'url': reverse('electric_car')
            },
        ]
    }
    return HttpResponse(get_template("shop/catalogue.html").render(context, request))


def order(request):
    context = {'title': 'Замовлення'}
    return HttpResponse(get_template("shop/order.html").render(context, request))


def bmw(request):
    context = {
        'title': 'BMW',
        'cars': [
            {
                'image': '/static/img/bmw/images.jfif',
                'name': 'BMW 3 Series',
                'description': {
                    'type': 'Седан',
                    'engine': '2.0 L I4 Turbo',
                    'power': '255',
                    'dispersal': '5.6',
                    'fuel_consumption': ' 7.5 л/100 км (місто), 5.0 л/100 км (трасса)',
                    'price_month': '1500',
                },
                'url': reverse('order'),
            },
            {
                'image': '/static/img/bmw/1614846802162.jpg',
                'name': 'BMW X5',
                'description': {
                    'type': 'Кросовер',
                    'engine': '3.0 L I6 Turbo',
                    'power': '335',
                    'dispersal': '5.5',
                    'fuel_consumption': '0-100 км/год: 5.2 секунд',
                    'price_month': '2100',
                },
                'url': reverse('order'),
            }
        ]
    }
    return HttpResponse(get_template("shop/bmw.html").render(context, request))


def mercedes(request):
    context = {
        'title': 'Mercedes',
        'cars': [
        {
            'image': '/static/img/mercedes/Mercedes-Benz-rest-S-class-w222-TopRent.UA_1.jpg',
            'name': 'Mercedes-Benz S-Class',
            'description': {
                'type': 'Люкс-седан',
                'engine': '3.0 L I6 Turbo',
                'power': '429 к.с.',
                'dispersal': '5.1 секунд (0-100 км/год)',
                'fuel_consumption': '9.8 л/100 км',
                'price_month': '2500 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/mercedes/mercedes-benz-e-class-limousine-12.jpeg',
            'name': 'Mercedes-Benz E-Class',
            'description': {
                'type': 'Середній клас',
                'engine': '2.0 L I4 Turbo',
                'power': '255 к.с.',
                'dispersal': '6.3 секунд (0-100 км/год)',
                'fuel_consumption': '8.1 л/100 км',
                'price_month': '2100 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/mercedes/mercedes-benz-a-class-limousine-1.jpg',
            'name': 'Mercedes-Benz A-Class',
            'description': {
                'type': 'Компакт',
                'engine': '2.0 L I4 Turbo',
                'power': '188 к.с.',
                'dispersal': '7.5 секунд (0-100 км/год)',
                'fuel_consumption': '6.2 л/100 км',
                'price_month': '1800 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/mercedes/822f3bdb711591d9f918ebdecc9019f1.jpg',
            'name': 'Mercedes-Benz G-Class',
            'description': {
                'type': 'Позашляховик',
                'engine': '4.0 L V8 Turbo',
                'power': '416 к.с.',
                'dispersal': '5.6 секунд (0-100 км/год)',
                'fuel_consumption': '13.1 л/100 км',
                'price_month': '3500 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/mercedes/1400x936.jpg',
            'name': 'Mercedes-Benz GLC',
            'description': {
                'type': 'Кросовер',
                'engine': '2.0 L I4 Turbo',
                'power': '255 к.с.',
                'dispersal': '6.2 секунд (0-100 км/год)',
                'fuel_consumption': '9.2 л/100 км',
                'price_month': '2400 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/mercedes/mercedes-benz-c-class-w206-limousine-20.jpg',
            'name': 'Mercedes-Benz C-Class',
            'description': {
                'type': 'Седан',
                'engine': '2.0 L I4 Turbo',
                'power': '255 к.с.',
                'dispersal': '6.1 секунд (0-100 км/год)',
                'fuel_consumption': '8.3 л/100 км',
                'price_month': '2000 USD/місяць',
            },
            'url': reverse('order'),
        }
    ]

    }
    return HttpResponse(get_template("shop/mercedes.html").render(context, request))


def toyota(request):
    context = {
        'title': 'Toyota',
        'cars': [
        {
            'image': '/static/img/toyota/2020_Toyota_Corolla_LE_standard_front,_5.25.19.jpg',
            'name': 'Toyota Corolla',
            'description': {
                'type': 'Седан',
                'engine': '1.8 L I4',
                'power': '139 к.с.',
                'dispersal': '9.5 секунд (0-100 км/год)',
                'fuel_consumption': '7.6 л/100 км',
                'price_month': '1300 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/toyota/toyota_camry.jpg',
            'name': 'Toyota Camry',
            'description': {
                'type': 'Седан',
                'engine': '2.5 L I4',
                'power': '203 к.с.',
                'dispersal': '8.2 секунд (0-100 км/год)',
                'fuel_consumption': '8.0 л/100 км',
                'price_month': '1500 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/toyota/toyota_rav4.jpg',
            'name': 'Toyota RAV4',
            'description': {
                'type': 'Кросовер',
                'engine': '2.5 L I4',
                'power': '203 к.с.',
                'dispersal': '8.9 секунд (0-100 км/год)',
                'fuel_consumption': '8.2 л/100 км',
                'price_month': '1800 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/toyota/toyota_land_cruiser.jpg',
            'name': 'Toyota Land Cruiser',
            'description': {
                'type': 'Позашляховик',
                'engine': '5.7 L V8',
                'power': '381 к.с.',
                'dispersal': '6.7 секунд (0-100 км/год)',
                'fuel_consumption': '13.0 л/100 км',
                'price_month': '3500 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/toyota/toyota_highlander.jpg',
            'name': 'Toyota Highlander',
            'description': {
                'type': 'Кросовер',
                'engine': '3.5 L V6',
                'power': '295 к.с.',
                'dispersal': '7.3 секунд (0-100 км/год)',
                'fuel_consumption': '9.5 л/100 км',
                'price_month': '2500 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/toyota/toyota_prius.jpg',
            'name': 'Toyota Prius',
            'description': {
                'type': 'Гібрид',
                'engine': '1.8 L I4 + електродвигун',
                'power': '121 к.с.',
                'dispersal': '10.0 секунд (0-100 км/год)',
                'fuel_consumption': '4.4 л/100 км',
                'price_month': '1700 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/toyota/toyota_avalon.jpg',
            'name': 'Toyota Avalon',
            'description': {
                'type': 'Люкс-седан',
                'engine': '3.5 L V6',
                'power': '301 к.с.',
                'dispersal': '6.0 секунд (0-100 км/год)',
                'fuel_consumption': '8.1 л/100 км',
                'price_month': '2200 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/toyota/toyota_4runner.jpg',
            'name': 'Toyota 4Runner',
            'description': {
                'type': 'Позашляховик',
                'engine': '4.0 L V6',
                'power': '270 к.с.',
                'dispersal': '7.5 секунд (0-100 км/год)',
                'fuel_consumption': '12.0 л/100 км',
                'price_month': '2800 USD/місяць',
            },
            'url': reverse('order'),
        }
    ]
}
    return HttpResponse(get_template("shop/toyota.html").render(context, request))


def electric_car(request):
    context = {
        'title': 'Електроні машини',
        'cars': [
        {
            'image': '/static/img/electric/tesla_model_s.jpg',
            'name': 'Tesla Model S',
            'description': {
                'type': 'Електричний седан',
                'engine': 'Dual Motor All-Wheel Drive',
                'power': '1020 к.с.',
                'dispersal': '2.1 секунд (0-100 км/год)',
                'fuel_consumption': '18.2 кВт⋅год/100 км',
                'price_month': '4000 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/electric/nissan_leaf.jpg',
            'name': 'Nissan Leaf',
            'description': {
                'type': 'Електричний хетчбек',
                'engine': '100 kW Electric Motor',
                'power': '147 к.с.',
                'dispersal': '7.9 секунд (0-100 км/год)',
                'fuel_consumption': '15.0 кВт⋅год/100 км',
                'price_month': '2200 USD/місяць',
            },
            'url': reverse('order'),
        },
        {
            'image': '/static/img/electric/chevrolet_bolt_ev.jpg',
            'name': 'Chevrolet Bolt EV',
            'description': {
                'type': 'Електричний хетчбек',
                'engine': '200 hp Electric Motor',
                'power': '200 к.с.',
                'dispersal': '6.5 секунд (0-100 км/год)',
                'fuel_consumption': '16.5 кВт⋅год/100 км',
                'price_month': '2500 USD/місяць',
            },
            'url': reverse('order'),
        }
    ]
    }
    return HttpResponse(get_template("shop/electric-car.html").render(context, request))

