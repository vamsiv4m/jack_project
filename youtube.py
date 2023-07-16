from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Speech import speak
from Listen import take_command

def youtube():
    speak("which video do you want to watch?")
    text=take_command().lower()
    driver=webdriver.Firefox(executable_path=r"C:\Users\HP\OneDrive\Desktop\jack voice assistant\geckodriver.exe")
    driver.maximize_window()
    driver.get(f"https://www.youtube.com/results?search_query={text}")
    wait=WebDriverWait(driver,100)
    wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="dismissible"]'))).click()
    try:
        wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="skip-button:5"]/span/button'))).click()
    except Exception:
        pass

