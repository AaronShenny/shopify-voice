from tkinter import *
from PIL import Image, ImageTk
import speech_recognition as sr

def quitGame(event):
    canvas.itemconfig(quitButton, image=gifImage)  # Change to GIF
    root.after(100, listen_for_input)  # Schedule the listen_for_input function after a short delay
    root.after(3000, restoreImage)  # Schedule the restoration after 3000 milliseconds (3 seconds)

def restoreImage():
    canvas.itemconfig(quitButton, image=quitImage)  # Change back to the original image

def listen_for_input():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 3000  # Adjust this value based on your environment

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        print('Listening...')
        audio = recognizer.listen(source, timeout=5)
        print('Processing...')
        user_input = recognizer.recognize_google(audio).lower()
        print(user_input)

root = Tk()
root.title("Shopify")
root.geometry('850x450')
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Source Code', command=lambda: aaron())  # Changed the command to use lambda
helpmenu.add_command(label='About')

# Create a Canvas widget
canvas = Canvas(root, width=850, height=450, bg='black')
canvas.pack()

# Load button image with transparency
quitImage = Image.open("img/mic.jpg")
quitImage = quitImage.resize((50, 50), Image.LANCZOS)
quitImage = ImageTk.PhotoImage(quitImage)

# Load GIF image
gifImage = Image.open("img/Sound.gif")
gifImage = gifImage.resize((50, 50), Image.LANCZOS)
gifImage = ImageTk.PhotoImage(gifImage)

# Create a button with the original image
quitButton = canvas.create_image(150, 90, image=quitImage)
canvas.tag_bind(quitButton, "<Button-1>", quitGame)

root.mainloop()
