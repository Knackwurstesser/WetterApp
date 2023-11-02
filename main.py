#Dieses Programm holt mir die aktuellen Wetterdaten von Openweather.org
#Die Parameter sind Breitengrad, Längengrad und die Spracheinstellungen
#Erforderliche Bibliothek = requests und customtkinter
#Erstellt am 16.10.2023 von R.H.
import customtkinter as custk
import requests

#Deklarationsteil

custk.set_appearance_mode("dark")  # Modis: system (Standard), light, dark
custk.set_default_color_theme("blue")  # Themes: blue (Standard), dark-blue, green

def button_callback():
    print("Button click", combobox_1.get())


#def slider_callback(value):
    #progressbar_1.set(value)

API_Key = "ba547e76c14656bedf4e71bc77865d49" # API-Key muss bei Openweather.org geholt werden - registrieren !

#Ort Gillenfeld

lat = "50.1283873" #Breitengrad
lon = "6.9045258" #Längengrad
lang = "de" #Spracheinstellungen

'''#Ort Koblenz
lat = "50.3569429"
lon = "7.5889959"
lang = "de"'''

#Aufruf der Wetter-Api - Der f-String erlaubt die Nutzung von Variablen in HTTP-Requests !
request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}&lang={lang}"
response = requests.get(request_url) #Ausführen der Anfrage

if response.status_code == 200: #Code 200 steht für OK
    data = response.json() # Hier werden die empfangenen Daten in data geschrieben.
    print(data) # Hier werden die Daten an die Konsole ausgegeben
    weather_description = data["weather"][0]["description"] #Hier wird die Wetterbeschreibung ausgelesen
    #print("An Ihren gewählten Koordinaten ist es : ",weather_description) # Hier wird die Wetterbeschreibung an die Konsole ausgegeben
    ausgabe = "An Ihren gewählten Ort ist es : {0}\n".format(weather_description)

    temperature = round(data["main"]["temp"]-273.15) #Hier wird die Temperatur ausgelesen und Kelvin abgezogen!
    #print("Die aktuelle Temperatur beträgt : ",temperature, "°C") # Hier wird die Temperatur an die Konsole ausgegeben
    ausgabe1 = ausgabe + "Die aktuelle Temperatur beträgt : {0}°C\n".format(temperature)
    humidity = data["main"]["humidity"]  # Hier wird die Luftfeuchtigkeit ausgelesen
    #print("Die Luftfeuchtigkeit beträgt : ", humidity, "%") #Hier wird die Luftfeuchtigkeit ausgegeben

    ausgabe2 = ausgabe1 + "Die Luftfeuchtigkeit beträgt : {0}%".format(humidity)

    print(ausgabe2)

else:
    print("Fehler mit folgendem Code : ", response.status_code) #Falls die Abfrage Fehler erhalten hat, dann wird das hier ausgegeben!
    pass #Ausgeben des Fehlers reicht zunächst aus !



#Hauptprogramm

root = custk.CTk()#Initialisierung des Fensters
root.geometry("400x350")#Einstellung der Größe des Fensters
root.title("Your daily Weather ...")#Titel des Fensters
root.minsize(width=400,height=350)#Minimumgröße des Fensters


frame_1 = custk.CTkFrame(master=root)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = custk.CTkLabel(master=frame_1, justify=custk.LEFT,text="Bitte wählen Sie Ihren Ort aus : ")
label_1.pack(pady=10, padx=10)

combobox_1 = custk.CTkComboBox(frame_1, values=["Gillenfeld", "Koblenz", "weitere Orte..."]) #Werte für Combobox - SQL möglich
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Gillenfeld") #Defaultwert

button_1 = custk.CTkButton(master=frame_1, command=button_callback, text="Wetter anzeigen")
button_1.pack(pady=10, padx=10)

text_1 = custk.CTkTextbox(master=frame_1, width=280, height=70)
text_1.pack(pady=10, padx=10)
#text_1.insert("0.0", "Hier stehen Ihre Daten drin\n\n\n\n")
text_1.insert("0.0", ausgabe2)

button_2 = custk.CTkButton(master=frame_1, command=root.destroy, text="Schließen")#Schließen des Hauptfensters
button_2.pack(pady=10, padx=10)

root.mainloop()
