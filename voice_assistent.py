import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak and print
def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to take voice input and print it
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}")
    except:
        print("Sorry, could not understand.")
        speak("Sorry, I could not understand. Please say that again.")
        return "None"
    return query.lower()

# Greet the user with both audio and terminal output
def greet_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("How can I help you?")

# Main assistant logic
def run_assistant():
    greet_user()
    while True:
        command = take_command()

        if command == "none":
            continue

        if "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time}")

        elif "wikipedia" in command:
            speak("Searching Wikipedia...")
            try:
                result = wikipedia.summary(command.replace("wikipedia", ""), sentences=2)
                speak(result)
            except:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif "open youtube" in command:
            speak("Opening YouTube...")
            webbrowser.open("https://www.youtube.com")

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I didn't get that.")

if __name__ == "__main__":
    run_assistant()
