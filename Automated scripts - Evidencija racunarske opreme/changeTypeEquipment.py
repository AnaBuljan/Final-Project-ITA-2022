'''Automated test script that creates new type of equipment in website section 'Tip/Proizvodjac opreme' on website
'Evidencija Racunarske Opreme'. After new type of equipment is registered, the script chooses that type and changes
it to another type. '''

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
movetoType = driver.find_element(By.CSS_SELECTOR, "#wrapper > header > nav > ul:nth-child(1) > li:nth-child(4) > a")
movetoType.click()

time.sleep(1)
openType = driver.find_element(By.CSS_SELECTOR, "#wrapper > div:nth-child(2) > div:nth-child(1) > label")
openType.click()

time.sleep(1)
enterTypeEquip = driver.find_element(By.NAME, "equiptype")
enterTypeEquip.click()
enterTypeEquip.send_keys("Konzola")

time.sleep(2)
saveType = driver.find_element(By.NAME, "saveEquipType")
saveType.click()

time.sleep(2)
openTypeAgain = driver.find_element(By.CSS_SELECTOR, "#wrapper > div:nth-child(2) > div:nth-child(1) > label")
openTypeAgain.click()

time.sleep(2)
openChangePopup = driver.find_element(By.CSS_SELECTOR, "#myTable > tbody > tr:nth-child(16) > td:nth-child(3) > button:nth-child(1)")
openChangePopup.click()

time.sleep(1)
changeType = driver.find_element(By.CSS_SELECTOR, "#modaltype > div > div.modal-body > div > form > input[type=text]:nth-child(1)")
changeType.click()
changeType.send_keys(Keys.CONTROL + "a")
changeType.send_keys(Keys.DELETE)
changeType.send_keys("Printer")

time.sleep(1)
saveChange = driver.find_element(By.NAME, "updateType")
saveChange.click()

time.sleep(2)
logout = driver.find_element(By.CLASS_NAME, "logout")
logout.click()

driver.quit()