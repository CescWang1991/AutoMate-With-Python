#! python3
# quickWeather.py - Prints the weather for a location from the command line.
import json, requests, sys, pprint
# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(('London','UK'))

# TODO: Download the JSON data from OpenWeatherMap.org's API.
url ='http://samples.openweathermap.org/data/2.5/weather?q=%s,uk&appid=b6907d289e10d714a6e88b30761fae22' % (location)
response = requests.get(url)
response.raise_for_status()

# TODO: Load JSON data into a Python variable.
weatherData = json.loads(response.text)
w = weatherData['main']
print('Current weather in %s:' % (location))
pprint.pprint(w)
