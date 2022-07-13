'''Automated test script that chooses one employee from website section 'Zaposleni - Zaduzivanje/Razduzivanje
and assigns a piece of equipment on website 'Evidencija Racunarkse Opreme'. The second step is to decommission 
the same piece of equipment. '''

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

time.sleep(2)
decommissionEquip = driver.find_element(By.CSS_SELECTOR, "#results > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > button.button.blue")
decommissionEquip.click()

time.sleep(2)
chooseEquip = driver.find_element(By.ID, "1")
chooseEquip.click()

time.sleep(1)
addEquip = driver.find_element(By.NAME, "obligation")
addEquip.click()

time.sleep(2)
decommissionEquip = driver.find_element(By.CSS_SELECTOR, "#results > div > table > tbody > tr:nth-child(2) > td:nth-child(8) > button.button.blue")
decommissionEquip.click()

time.sleep(2)
removeEquip= driver.find_element(By.ID, "1")
removeEquip.click()

time.sleep(2)
confirmRemove = driver.find_element(By.NAME, "obligateEquipE")
confirmRemove.click()

time.sleep(2)
logout = driver.find_element(By.CLASS_NAME, "logout")
logout.click()

driver.quit()