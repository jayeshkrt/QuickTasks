import requests
import urllib.parse

# address = 'Bir, MP, India'

def weather_update(address):
    """
    @param address (string): Format will be-> city, state, country [with commas]
    @returns (string): weather updates for that city
    """
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

    response = requests.get(url).json()
    # print(response)
    lat = response[0]["lat"]
    lon = response[0]["lon"]

    url_weather = 'https://api.openweathermap.org/data/2.5/onecall?lat='+lat+'&lon='+lon+'&exclude=minutely,hourly,alerts&units=metric&appid=0a5a921b3eb9db0c50111ae9a3ff8e59'
    response = requests.get(url_weather).json()
    output = "Current condition: "+ response['current']['weather'][0]['main'] + "\nDescription: "+ response['current']['weather'][0]['description']
    output += "\nTemperature: "+str(response['current']['temp'])+" degrees"+"\nHumidity: "+ str(response['current']['humidity'])+"%"
    output += "\nMinimum: "+str(response['daily'][0]['temp']['min'])+" degrees"+"\nMaximum: "+str(response['daily'][0]['temp']['max'])+" degrees"+"\n"
    return (output)

