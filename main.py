import requests
from twilio.rest import Client

API_KEY = "your_openweather_api_key"
URL = "http://api.openweathermap.org/data/2.5/forecast"
# http://api.openweathermap.org/data/2.5/forecast?lat=16.81&lon=74.56&appid=your_api_id

SID = "your_twilio_sid"
TOKEN = "your_twilio_token"
P_NUM = "your_twilio phone_number"

MY_LAT = 16.815304
MY_LNG = 74.569595


parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": API_KEY,
    "cnt": 4,
}

respond = requests.get(url=URL, params=parameters)
respond.raise_for_status()

weather_data = respond.json()
will_rain = False

for lst in weather_data['list']:
    weather_id = lst['weather'][0]['id']
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(SID, TOKEN)
    message = client.messages.create(to="receiver_number", from_=P_NUM,
                                     body="It's going to be rain today ⛈️. Bring your ☂️")
    print(message.status)
