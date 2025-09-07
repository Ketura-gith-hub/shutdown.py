import os
import sys
import pyttsx3
import time

engine = pyttsx3.init()

engine.say("Do you want to shutdown your computer? Type yes or no.")
engine.runAndWait()

check = input("Do you want to shutdown your computer? (Yes/No or 1/0): ")

if check.lower() in ["no", "0"]:
    engine.say("Okay, I will not shut down the computer.")
    engine.runAndWait()

    check = input(" Okay, I will not shut down the computer.")

    sys.exit(0)

elif check.lower() in ["yes", "1"]:
    engine.say("Shutting down your computer now.")
    engine.runAndWait()
    os.system("shutdown /s /t 1")

else:
    engine.say("Invalid input. Please type Yes, No, 1, or 0.")
    engine.runAndWait()
    print("Invalid input. Please type Yes/No or 1/0.")