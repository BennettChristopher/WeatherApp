import tkinter as tk
from tkinter import *
import requests
import time
import datetime


def getData(self):
    city = inputbox.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    city = json_data['name']
    country = json_data['sys']['country']
    temperature = int(json_data['main']['temp'] - 273.15)
    icon = json_data['weather'][0]['icon']
    weather = json_data['weather'][0]['main']
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    timezone = json_data['timezone']
    timedifference = timezone - 19800
    sunrise = time.strftime('%H:%M', time.gmtime(
        json_data['sys']['sunrise'] + timezone))
    sunset = time.strftime('%H:%M', time.gmtime(
        json_data['sys']['sunset'] + timezone))

    final_info = city + ", " + country + "\n" + str(temperature) + "°C"
    final_data = "\n" + weather + "\n" + "Min/Max: " + str(min_temp)+"/"+str(max_temp) + "°C" + "\n" + "Humidity: " + str(
        humidity) + "%" + "\n" + "Wind Speed: " + str(wind) + "km/h \n" + "Sunrise: " + sunrise + "hrs \n" + "Sunset: " + sunset + "hrs"+"\nLocal Time: "+getTime(timedifference)

    label1.config(text=final_info)
    label3.config(text=final_data)

    image = PhotoImage(file=f"resources/icons/{icon}.png")
    label2.config(image=image, bg="sky blue")
    label2.image = image


# structure
app = tk.Tk()
app.geometry("360x480")
app.title("Weather App.")
app.resizable(False, False)
app.iconbitmap("resources/icon.ico")
app.config(bg="sky blue")

# fonts
font0 = ("Calibri", 10, "bold", "italic")
font1 = ("Calibri", 15, "bold")
font2 = ("Calibri", 20, "bold")
font3 = ("Calibri", 30, "bold")

# input
inputbox = tk.Entry(app, font=font1, bg="white", width=50, text="Bengaluru")
inputbox.pack(padx=25, pady=10)
inputbox.focus()
inputbox.bind('<Return>', getData)

# labels
label0 = tk.Label(app, font=font0, bg="sky blue", text="enter city name...")
label0.pack()
label1 = tk.Label(app, font=font3, bg="sky blue")
label1.pack()
label2 = tk.Label(app)
label2.pack()
label3 = tk.Label(app, font=font1, bg="sky blue")
label3.pack()


def getTime(timedifference):
    now = time.time()
    localtime = now + timedifference
    timestr = datetime.datetime.strptime(
        time.ctime(localtime), "%a %b %d %H:%M:%S %Y")
    timestr = timestr.strftime("%H:%Mhrs %a, %d %b %Y")
    return timestr


app.mainloop()
