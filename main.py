import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
speak.Speak("Welcome to Weather Forcast App 2 point o developed by AMAN RAJ SHARMA")
while True:
    speak.Speak("Enter your City")
    city = input("Enter the Name of the City\n")
    url = f"https://api.weatherapi.com/v1/current.json?key=e15d594e2f224aa3bf9222121231506&q={city}"
    r = requests.get(url)
    # print(r.text)
    # converting into a dictionary:
    WeatherDict = json.loads(r.text)
    text = WeatherDict["current"]["temp_c"]
    speak.Speak(f"The temperature in {city} is {text} degree Celsius")
    print(text)
    speak.Speak(f"Want to know any other city?")
    y = input("Want to know any other city?")
    if y == 'yes':
        continue
    else:
        speak.Speak(f"Thanks For using Weather Forcast App 2 point O")
        print("Thanks For using Weather Forcast App 2.0")
        break
