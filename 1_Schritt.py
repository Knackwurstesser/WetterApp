import requests

API_Key = "ba547e76c14656bedf4e71bc77865d49"

#Gillenfeld
lat = "50.1283873" #Breitengrad
lon = "6.9045258" #Längengrad
lang = "DE"

request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}&lang={lang}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    #print(data)
    weather_description = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 273.15)
    humidity = data["main"]["humidity"]
    print("An den gewählten Koordinaten ist es : ", weather_description)
    print("Die aktuelle Temperatur beträgt : ", temperature, "°C")
    print("Die Luftfeuchtigkeit beträgt : ", humidity, "%")

else:
    print("Fehler mit folgendem Code : ", response.status_code)
    pass


