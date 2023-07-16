from time import sleep
import datetime
import random
from Speech import speak
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Encrypt_Decrypt import Encrypt_Decrypt
responses=["don't fear! when I'm here...",
"Just have a cup of coffee...I will do it...",
"Sure, I will do it"]
def timesheet(): 
    speak(random.choices(responses))   
    day=datetime.datetime.now()
    day=day.strftime("%A").lower()
    print(day.capitalize())
    if(day=="saturday" or day=="sunday"):
        print("Its weekend no need to fill timesheet")
    else:
        driver=webdriver.Chrome(r'C:\Users\HP\OneDrive\Desktop\jack voice assistant\chromedriver.exe')
        driver.maximize_window()
        driver.get("https://timesheet.ultimatix.net/timesheet/Login/bridge?")
        myempid=1987657
        wait=WebDriverWait(driver,8)
        wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="form1"]'))).send_keys(myempid)
        wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="proceed-button"]'))).click()
        sleep(3)
        driver.execute_script("passwordValue()")
        passwd=Encrypt_Decrypt().get_decode()
        wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="password-login"]'))).send_keys(passwd)
        wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="form-submit"]'))).click()
        hours=9
        wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="effortUnassign01"]'))).clear()
        wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="effortUnassign01"]'))).send_keys(hours)
        wait.until(ec.visibility_of_element_located((By.XPATH,'//*[@id="layout_pageContent"]/div/div/div[8]/div[2]/div[3]/div[8]/span[1]/input'))).click()
        sleep(5)
        speak("Your timesheet filled successfully ...")