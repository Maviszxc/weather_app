import requests

from django.conf import settings


# Replace with your own API key

def current_weather(request, city_name='Makati'):
    
    payload = {
        'key': 'f3ae3bf833d14558b1e15421240502',
        'q': city_name,
    }
    response = requests.get('http://api.weatherapi.com/v1/current.json', params=payload)
    
    print(response.status_code)
    print(response.url)
    
    
    return response.json()




def forecast_weather(request, city_name='Makati'):
    payload = {
        'key': 'f3ae3bf833d14558b1e15421240502',
        'q': city_name,
        'days': 3,
    }
    response = requests.get('http://api.weatherapi.com/v1/forecast.json', params=payload)
    print(response.status_code)
    print(response.url)
    return response.json()

    