# 2nd_Step_Daten_formatieren.py
# Wir haben die Daten erfolgreich beziehen können.
# Doch mit diesen Daten können wir so nichts anfangen und müssen die
# für eine Ausgabe an die Konsole filtern/formatieren
import requests

API_Key = "ba547e76c14656bedf4e71bc77865d49" # API-Key muss bei Openweather.org geholt werden - registrieren !

#Ort Gillenfeld

lat = "50.1283873" #Breitengrad
lon = "6.9045258" #Längengrad
lang = "de" #Spracheinstellungen

#Aufruf der Wetter-Api - Der f-String erlaubt die Nutzung von Variablen in HTTP-Requests !
request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}&lang={lang}"
response = requests.get(request_url) #Ausführen der Anfrage

if response.status_code == 200: #Code 200 steht für OK
    data = response.json() # Hier werden die empfangenen Daten in data geschrieben.
    print(data) # Hier werden die Daten an die Konsole ausgegeben
    weather_description = data["weather"][0]["description"]  # Hier wird die Wetterbeschreibung ausgelesen
    temperature = round(data["main"]["temp"] - 273.15)  # Hier wird die Temperatur ausgelesen und Kelvin abgezogen!
    humidity = data["main"]["humidity"]  # Hier wird die Luftfeuchtigkeit ausgelesen
    print("An Ihren gewählten Koordinaten ist es : ",weather_description) # Hier wird die Wetterbeschreibung an die Konsole ausgegeben
    print("Die aktuelle Temperatur beträgt : ",temperature, "°C") # Hier wird die Temperatur an die Konsole ausgegeben
    print("Die Luftfeuchtigkeit beträgt : ", humidity, "%") #Hier wird die Luftfeuchtigkeit ausgegeben
else:# alle anderen Codes bedeuten, dass die Anfrage nicht durchgeführt wurde
    print("Fehler mit folgendem Code : ", response.status_code) #Falls die Abfrage Fehler erhalten hat, dann wird das hier ausgegeben!
    pass #Ausgeben des Fehlers reicht zunächst aus !
