# 1st_Step_API.py
# Wir wollen zunächst eine Verbindung zum Anbieter für die Wetterdaten herstellen
# und uns die Daten aus geben.
# Wir benötigen dafür die Bibliothek requests, die wir vorher schon installiert haben
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

else:# alle anderen Codes bedeuten, dass die Anfrage nicht durchgeführt wurde
    print("Fehler mit folgendem Code : ", response.status_code) #Falls die Abfrage Fehler erhalten hat, dann wird das hier ausgegeben!
    pass #Ausgeben des Fehlers reicht zunächst aus !
