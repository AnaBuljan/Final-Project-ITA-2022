'''Automated test script that creates a new user profile on website section 'Administracija Korisnika' on website
'Evidencija Racunarske Opreme'. The same user profile is then deleted. '''

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
userAdministration = driver.find_element(By.CSS_SELECTOR, "#wrapper > header > nav > ul:nth-child(1) > li:nth-child(6) > a")
userAdministration.click()

time.sleep(2)
firstNameUser = driver.find_element(By.CSS_SELECTOR, "#wrapper > div.section-one-left > form > input[type=text]:nth-child(2)")
lastNameUser = driver.find_element(By.CSS_SELECTOR, "#wrapper > div.section-one-left > form > input[type=text]:nth-child(3)")
userNameUser = driver.find_element(By.CSS_SELECTOR, "#wrapper > div.section-one-left > form > input[type=text]:nth-child(4)")
passWordUser = driver.find_element(By.CSS_SELECTOR, "#wrapper > div.section-one-left > form > input[type=password]:nth-child(5)")

firstNameUser.send_keys("anaTest")
lastNameUser.send_keys("buljanTest")
userNameUser.send_keys("AnaAuto")
passWordUser.send_keys("anaauto")

rolePick = driver.find_element(By.ID, "role")
rolePick.click()

roleUser = driver.find_element(By.CSS_SELECTOR, "#role > option:nth-child(3)")
roleUser.click()

saveUser = driver.find_element(By.CSS_SELECTOR, "#wrapper > div.section-one-left > form > input.button.blue")
saveUser.click()

time.sleep(2)
deleteUser = driver.find_element(By.CSS_SELECTOR, "#wrapper > div.section-two > div > table > tbody > tr:nth-child(23) > td:nth-child(6) > button.button.red")
deleteUser.click()

time.sleep(2)
deleteConfirm = driver.find_element(By.ID, "del")
deleteConfirm.click()

time.sleep(2)
logout = driver.find_element(By.CLASS_NAME, "logout")
logout.click()

driver.quit()