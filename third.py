import requests
import json
import pyttsx3

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)
current_temperature = wdic["current"]["temp_c"]

message = f"Current temperature in {city} is {current_temperature} degrees Celsius."

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Say the message
engine.say(message)

# Wait for the speech to finish
engine.runAndWait()
