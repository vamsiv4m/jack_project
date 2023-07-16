from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Encrypt_Decrypt import Encrypt_Decrypt
driver=webdriver.Chrome(r"C:\Users\HP\OneDrive\Desktop\jack voice assistant\chromedriver.exe")
driver.get("https://www.facebook.com")
wait=WebDriverWait(driver ,10)
sleep(5)
driver.close()
# wait.until(ec.visibility_of_element_located((B)))