from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re, pyttsx3



def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 180)


def google_search(command):
    reg_ex = re.search('search google for (.*)', command)
    if reg_ex:
        search_for = reg_ex.group(1)
        url = 'https://www.google.com/'
        url += 'search?q=' + search_for.replace(" ", "+")
        speak("Okay sir!")
        speak(f"Searching for {search_for}")
        driver = webdriver.Chrome(executable_path='driver/chromedriver.exe')
        driver.get(url)



# google_search("search google for Virat Kohli")
