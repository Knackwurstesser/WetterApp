# 4th_Step_SQL.py
from tkinter import END
import requests
import customtkinter
import backend

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

backend.connect() #Initialisieren der Datenbank
ausgabe3 = [] #Initialisierung als Liste

for daten in backend.view(): #holen der Einträge aus der Datenbank
    ausgabe3.append(daten[1]) #Jeden Eintrag an die Listen hängen

def button_callback():
 wetter_abrufen(combobox_1.get())
def wetter_abrufen(ort):
 cords = backend.cords(ort)# Hier werden die Koordinaten des Ortes abgerufen
 lat = cords[0][0] #Daten werden als Tupel geliefert !
 lon = cords[0][1]

 API_Key = "ba547e76c14656bedf4e71bc77865d49" # API-Key muss bei Openweather.org geholt werden - registrieren !
 lang = "de" #Spracheinstellung andere möglich

 #Aufruf der Wetter-Api - Der f-String erlaubt die Nutzung von Variablen in HTTP-Requests !
 request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}&lang={lang}"
 response = requests.get(request_url) #Ausführen der Anfrage

 if response.status_code == 200: #Code 200 steht für OK
     data = response.json() # Hier werden die empfangenen Daten in data geschrieben.
     #print(data) # Hier werden die Daten an die Konsole ausgegeben
     weather_description = data["weather"][0]["description"]  # Hier wird die Wetterbeschreibung ausgelesen
     temperature = round(data["main"]["temp"] - 273.15)  # Hier wird die Temperatur ausgelesen und Kelvin abgezogen!
     humidity = data["main"]["humidity"]  # Hier wird die Luftfeuchtigkeit ausgelesen
     #print("An Ihren gewählten Koordinaten ist es : ",weather_description) # Hier wird die Wetterbeschreibung an die Konsole ausgegeben
     ausgabe = "An Ihren gewählten Koordinaten ist es :\n{0}\n".format(weather_description)
     #print("Die aktuelle Temperatur beträgt : ",temperature, "°C") # Hier wird die Temperatur an die Konsole ausgegeben
     ausgabe1 = ausgabe + "Die aktuelle Temperatur beträgt : {0}°C\n".format(temperature)
     #print("Die Luftfeuchtigkeit beträgt : ", humidity, "%") #Hier wird die Luftfeuchtigkeit ausgegeben
     ausgabe2 = ausgabe1 + "Die Luftfeuchtigkeit beträgt : {0}%".format(humidity)
     text_1.delete("0.0", END) #Löschen des Inhaltes der Textbox sont wird angehangen !
     text_1.insert("0.0", ausgabe2)#Ausgabe der ermittelten Wetterdaten

 else:# alle anderen Codes bedeuten, dass die Anfrage nicht durchgeführt wurde
     print("Fehler mit folgendem Code : ", response.status_code) #Falls die Abfrage Fehler erhalten hat, dann wird das hier ausgegeben!
     pass #Ausgeben des Fehlers reicht zunächst aus !

#Hauptprogramm

root = customtkinter.CTk()
root.title("Weather App")
root.geometry("400x400")

frame1 = customtkinter.CTkFrame(master=root)
frame1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame1, justify=customtkinter.LEFT, text="Bitte wählen Sie einen Ort aus : ")
label_1.pack(pady=10, padx=10)

#combobox_1 = customtkinter.CTkComboBox(frame1, values=["Gillenfeld","Koblenz","Köln","Weitere Orte ..."])
combobox_1 = customtkinter.CTkComboBox(frame1, values=ausgabe3)
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Gillenfeld")

button_1 = customtkinter.CTkButton(master=frame1, command=button_callback, text="Wetter anzeigen")
button_1.pack(pady=10, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame1, width=280, height=90)
text_1.pack(pady=10, padx=10)
#text_1.insert("0.0", "Hier stehen Ihre Daten drin \n\n\n")


button_2 = customtkinter.CTkButton(master=frame1, command=root.destroy, text="Schließen")
button_2.pack(pady=10, padx=10)




root.mainloop()