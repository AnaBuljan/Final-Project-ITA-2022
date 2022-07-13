'''Template of login admin to use for all automated tests written for testing of 'Evidencija Racunarske Opreme'. '''

from selenium import webdriver 
import time 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("--disable-notification")

driver = webdriver.Chrome(chrome_options=option, executable_path='chromedriver.exe')

driver.get("https://puppies-closet.com/evidencija/login.php")

time.sleep(2)
usernameAdmin = driver.find_element(By.NAME, "username")
passwordAdmin = driver.find_element(By.NAME, "password")

usernameAdmin.send_keys("anabuljan")
passwordAdmin.send_keys("anabuljan123")

loginAdmin = driver.find_element(By.CLASS_NAME, "loginbutton")
loginAdmin.click()
