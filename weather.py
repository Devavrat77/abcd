import requests
import json
import pyttsx3
import speech_recognition as sr
r = sr.Recognizer()
speaker = pyttsx3.init()
# def weather(arg1, arg2):
def say(text):
    speaker.say(text)
    speaker.runAndWait()
    return


while True:
    try:
        # city = input("Enter the name of city\n => ")
        say("Temperature of which location would you like to know")
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, 0.4)
            audio_text = r.listen(source2)
            city = r.recognize_google(audio_text)
        print(city)
        if "no" in city:
            break
        url = f"http://api.weatherapi.com/v1/current.json?key=3d4c324339b34d56ab252220233103&q={city}"

        req = requests.get(url)
        d = json.loads(req.text)
        print(f"Temperature is : ", d["current"]["temp_c"])
        print("Weather is ", d["current"]["condition"]["text"])
        print("Wind speed is ", d["current"]["wind_mph"])
        print("Wind direction is ", d["current"]["wind_dir"])
        loc = d["location"]["name"]
        x = d["current"]["temp_c"]
        y = d["current"]["condition"]["text"]
        z = d["current"]["wind_mph"]
        e = d["current"]["wind_dir"]
        print("Location is", loc)
        rate = speaker.setProperty('rate', 150.0)
        volume = speaker.setProperty('volume', 3.0)
        speaker.say(f"{city} temperature is {x} degrees and Weather is {y} Wind speed"
                    f"is {z} Wind direction is in {e} ")
        speaker.runAndWait()
    except TypeError as t:
        print("type error")
    except ConnectionError as c:
        print("please check your connectivity")
    except SystemError as s:
        print("system Error")
    except Exception as e:
        while True:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, 0.6)
                say("sry i can't recognise it would you like to continue")
                except_text = r.listen(source2)
                bool = r.recognize_google(except_text)

                if "yes" in bool.lower():
                    x = "continue"
                    break
                elif "no" in bool.lower():
                    x = "no"
                    break
                else:
                    x = None
                    continue
        if x == "continue":
            continue
        else:
            break
