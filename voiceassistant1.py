import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser


listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    """Function to make the assistant speak."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Function to take a voice command from the user."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pranay' in command:
                command = command.replace('pranay', '').strip()
                print(command)
            return command
    except sr.RequestError:
        talk("Sorry, I couldn't connect to the internet.")
        return ""
    except sr.UnknownValueError:
        talk("Sorry, I didn't understand what you said.")
        return ""
    except Exception as e:
        talk(f"An error occurred: {str(e)}")
        return ""

def run_pranay():
    """Main function to run the Pranay voice assistant."""
    talk("Hi, I am Pranay, your voice assistant. How can I help you?")
    while True:
        command = take_command()
        if command:
            if 'play' in command:
                song = command.replace('play', '').strip()
                talk('Playing ' + song)
                print(f'Playing {song} on YouTube')
                try:
                    pywhatkit.playonyt(song)
                except Exception as e:
                    talk(f"Sorry, I couldn't play the song. {str(e)}")
            elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('The current time is ' + time)
                print(f'The current time is {time}')
            elif 'tell me about' in command:
                topic = command.replace('tell me about', '').strip()
                try:
                    info = wikipedia.summary(topic, sentences=2)
                    talk(info)
                    print(info)
                except Exception as e:
                    talk(f"Sorry, I couldn't find information on that topic. {str(e)}")
            elif 'open google' in command:
                talk('Opening Google')
                print('Opening Google')
                webbrowser.open('https://www.google.com')
            elif 'open spotify' in command:
                talk('Opening Spotify')
                print('Opening Spotify')
                webbrowser.open('https://www.spotify.com')
            elif 'open youtube' in command:
                talk('Opening YouTube')
                print('Opening YouTube')
                webbrowser.open('https://www.youtube.com')
            elif 'open wikipedia' in command:
                talk('Opening Wikipedia')
                print('Opening Wikipedia')
                webbrowser.open('https://www.wikipedia.org')
            elif 'who are you' in command:
                talk('I am your voice assistant Pranay.')
                print('I am your voice assistant Pranay.')
            elif 'what can you do' in command:
                talk('I can play songs, tell the time, provide information from Wikipedia, and open websites for you.')
                print('I can play songs, tell the time, provide information from Wikipedia, and open websites for you.')
            elif 'stop' in command:
                talk('Goodbye!')
                print('Goodbye!')
                break
            else:
                talk("Sorry, I didn't understand what you said. Can you repeat that?")
                print("Sorry, I didn't understand what you said. Can you repeat that?")

run_pranay()
