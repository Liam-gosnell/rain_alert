# import requests
# # from twilio.rest import Client



OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "55b3153418988acdcff82f75d89a844e"
account_sid = "ACf2e40d72f1ac688fbb62e1a041588b29"
auth_token = "57afea23a4ecdfe18f56fbaa84ec165a"

weather_params = {
    "lat": 51.908981,
    "lon": -8.258960,
    "appid": api_key,
    "exclude": "current,minute,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False


for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring an ☔️",
        from_='+12056495734',
        to='+353830808425'
    )

    # print(message.status)