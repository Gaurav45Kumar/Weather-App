import requests
import json
import os

city = input("Enter the name of city : ")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r=requests.get(url)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
