import requests
import json
import os
import win32api

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
current_temperature = wdic["current"]["temp_c"]

message = f"Current temperature in {city} is {current_temperature}°C"
win32api.MessageBox(0, message, "Weather Update", 0x40)  # 0x40 is the icon type (information)

print(message)
