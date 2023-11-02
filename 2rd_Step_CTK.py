# 3rd_Step_CTK.py
# Wir haben die Daten erfolgreich beziehen können.
# Doch mit diesen Daten können wir so nichts anfangen und müssen die
# für eine Ausgabe an die Konsole filtern/formatieren
import requests
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def button_callback():
 print("Button click", combobox_1.get())

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
    ausgabe = "An Ihren gewählten Koordinaten ist es :\n{0}\n".format(weather_description)
    print("Die aktuelle Temperatur beträgt : ",temperature, "°C") # Hier wird die Temperatur an die Konsole ausgegeben
    ausgabe1 = ausgabe + "Die aktuelle Temperatur beträgt : {0}°C\n".format(temperature)
    print("Die Luftfeuchtigkeit beträgt : ", humidity, "%") #Hier wird die Luftfeuchtigkeit ausgegeben
    ausgabe2 = ausgabe1 + "Die Luftfeuchtigkeit beträgt : {0}%".format(humidity)

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

combobox_1 = customtkinter.CTkComboBox(frame1, values=["Gillenfeld","Koblenz","Köln","Weitere Orte ..."])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Gillenfeld")

button_1 = customtkinter.CTkButton(master=frame1, command=button_callback, text="Wetter anzeigen")
button_1.pack(pady=10, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame1, width=280, height=90)
text_1.pack(pady=10, padx=10)
#text_1.insert("0.0", "Hier stehen Ihre Daten drin \n\n\n")
text_1.insert("0.0", ausgabe2)

button_2 = customtkinter.CTkButton(master=frame1, command=root.destroy, text="Schließen")
button_2.pack(pady=10, padx=10)




root.mainloop()