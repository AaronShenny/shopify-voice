import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\SPEECH_OneCore\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
engine.setProperty('rate', 120)

def respond(text):
    print(text)  # Print the message
    engine.say(text)  # Use pyttsx3 to speak the message
    engine.runAndWait()

def listen_for_input(username):
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 3000  # Adjust this value based on your environment

    with sr.Microphone() as source:
        # Adjust ambient noise for better recognition
        recognizer.adjust_for_ambien_noise(source)

        while True:
            try:
                print('Listening...')
                audio = recognizer.listen(source, timeout=5)  # Adjust the timeout for continuous listening
                print('Processing...')
                user_input = recognizer.recognize_google(audio).lower()
                print(user_input)

                if 'hey shopify' in user_input or 'shopify' in user_input:
                    respond(f'Hey {username}!')
                    respond('How can I help you?')
                    audio = recognizer.listen(source, timeout=5)
                    # Continue listening for further commandsgfvh
                    query = recognizer.recognize_google(audio, show_all=False).lower()
                    print(query)

                    return query, query.split()
                    

            except sr.UnknownValueError:
                print('UnknownValueError. Retrying...')
                continue
            except sr.WaitTimeoutError:
                print('Timeout. Retrying...')
                continue

if __name__ == '__main__':
    username = 'Aaron'
    query, tokens = listen_for_input(username)
    print(query, tokens)
