'''Automated test script that searches for a piece of equipment in wesbite sesction 'Tip/Proizvodjac opreme' on website
'Evidencija Racuarske Opreme'. The equipment is searched using serial number and then deleted.'''

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

time.sleep(1)
movetoEquipment = driver.find_element(By.CSS_SELECTOR, "#wrapper > header > nav > ul:nth-child(1) > li:nth-child(2) > a")
movetoEquipment.click()

time.sleep(2)
searchEquipment = driver.find_element(By.NAME, "equSearch")
searchEquipment.click()
searchEquipment.send_keys("JRO098")

time.sleep(1)
confirmSearch = driver.find_element(By.NAME, "equipmentSearch")
confirmSearch.click()

time.sleep(1)
deleteEquipment = driver.find_element(By.CSS_SELECTOR, "#results > div > table > tbody > tr:nth-child(3) > td:nth-child(10) > button.button.red")
deleteEquipment.click()

time.sleep(1)
deleteConfirm = driver.find_element(By.ID, "del")
deleteConfirm.click()

time.sleep(2)
logout = driver.find_element(By.CLASS_NAME, "logout")
logout.click()

driver.quit()