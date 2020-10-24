import json
import urllib.request

from django.shortcuts import render

API_KEY = ''  # TODO Add the API key


# Create your views here.
def home(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen(
            'http://api.weatherapi.com/v1/current.json?key=' + API_KEY + '&q=' + city).read()
        response = json.loads(source)
        print(response)
        data = {
            'name': str(response['location']['name']),
            'coordinates': {
                'longitude': str(response['location']['lon']),
                'latitude': str(response['location']['lat']),
            },
            'pressure': str(response['current']['pressure_mb']),
            'humidity': str(response['current']['humidity']),
            'wind': str(response['current']['wind_kph']),
            'temp_f': str(response['current']['temp_f']),
            'text': str(response['current']['condition']['text']),
            'local_time': str(response['location']['localtime']),
        }
    else:
        data = {}
    return render(request, 'weather.html', data)
