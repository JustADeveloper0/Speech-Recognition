import pyttsx3, time, speech_recognition

recognizer = speech_recognition.Recognizer()

def speak(phrase):
    engine = pyttsx3.init()
    engine.say(phrase)
    engine.runAndWait()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            print("Listening...")
            speak("Listening...")
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            new_text = text.lower()
            new_text = new_text.replace("to the power of","**")
            new_text = new_text.replace("^","**")
            new_text = new_text.replace("-","")
            
            if "√" in new_text:
                new_list = new_text.split()
                index = 0

                for i in new_list:
                    if i == "√":
                        break
                    index += 1

                new_list.insert(index + 2, "**")
                new_list.insert(index + 3, "0.5")

                index2 = 0
                for i in new_list:
                    if "√" in i:
                        new_list[index2] = new_list[index2].replace("√", "")
                    index2 += 1

                new_text = ""
                for i in new_list:
                    new_text += i + " "
            
            msg = None
            try: msg = eval(new_text)
            except: pass
            
            print(f"Recognized text: {text}")
            print(f"Response: {msg}")

            speak(f"Recognized text: {text}")
            speak(f"Response: {msg}")
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        continue
