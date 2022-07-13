'''Automated test script that registers new piece of equipment on website section dedicated to registering equipment 'Oprema'
on website 'Evidencija Racunarske Opreme'. '''

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
typeEquipment = driver.find_element(By.ID, "type_id")
typeEquipment.click()

chooseType = driver.find_element(By.CSS_SELECTOR, "#type_id > option:nth-child(4)")
chooseType.click()

time.sleep(1)
brandEquipment = driver.find_element(By.ID, "producer_id")
brandEquipment.click()

chooseBrand = driver.find_element(By.CSS_SELECTOR, "#producer_id > option:nth-child(12)")
chooseBrand.click()

time.sleep(1)
inventoryNumber = driver.find_element(By.NAME, "inventoryNumber")
serialNumber = driver.find_element(By.NAME, "serialNumber")

inventoryNumber.send_keys("1002")
serialNumber.send_keys("JRO098")

time.sleep(1)
saveEquipment = driver.find_element(By.NAME, "save")
saveEquipment.click()

time.sleep(2)
logout = driver.find_element(By.CLASS_NAME, "logout")
logout.click()

driver.quit()