import requests
import json
import pyttsx3
import speech_recognition as sr

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Function to get the city name from audio input
def get_city_from_audio():
    with sr.Microphone() as source:
        print("Please speak the name of the city...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)
    
    try:
        city_name = recognizer.recognize_google(audio)
        return city_name
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Error: {e}")
        return None

# Get the city name from audio input
city = get_city_from_audio()

if city:
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
