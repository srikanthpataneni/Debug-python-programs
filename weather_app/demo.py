import requests
import json
import tkinter as tk
from tkinter import Entry, Label, Button

def get_weather(city):
    api_key = "cc386124dfa9b8c75ecde6382cdc3b32"
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(base_url, params=params)
    data = json.loads(response.text)

    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result_label.config(text=f"Weather in {city}")
        description_label.config(text=f"Description: {description}")
        temperature_label.config(text=f"Temperature: {temperature}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
    else:
        result_label.config(text="City not found.")

app = tk.Tk()
app.title("Weather App")
app.geometry("500x500")

city_label = Label(app, text="Enter a city:")
city_label.pack(pady=10)

city_entry = Entry(app)
city_entry.pack()

fetch_button = Button(app, text="Fetch Weather", command=lambda: get_weather(city_entry.get()))
fetch_button.pack(pady=10)

result_label = Label(app, text="", font=("Helvetica", 16))
result_label.pack()

description_label = Label(app, text="", font=("Helvetica", 14))
description_label.pack()

temperature_label = Label(app, text="", font=("Helvetica", 14))
temperature_label.pack()

humidity_label = Label(app, text="", font=("Helvetica", 14))
humidity_label.pack()

wind_speed_label = Label(app, text="", font=("Helvetica", 14))
wind_speed_label.pack()

app.mainloop()
