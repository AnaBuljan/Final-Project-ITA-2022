'''Automated test script that creates a new piece of equipment on webiste section 'Tip/Proizvodjac opreme' 
on website 'Evidencija Racunarske Opreme' and deletes the same type again. '''

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
openBrand = driver.find_element(By.CSS_SELECTOR, "#wrapper > div:nth-child(2) > div:nth-child(2) > label")
openBrand.click()

time.sleep(2)
enterBrand = driver.find_element(By.NAME, "equipproducer")
enterBrand.click()
enterBrand.send_keys("Apple")

time.sleep(1)
saveBrand = driver.find_element(By.NAME, "saveEquipProducer")
saveBrand.click()

time.sleep(1)
openBrand = driver.find_element(By.CSS_SELECTOR, "#wrapper > div:nth-child(2) > div:nth-child(2) > label")
openBrand.click()

time.sleep(2)
deleteBrand = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]/div[2]/table/tbody/tr[15]/td[3]/button[2]")
deleteBrand.click()

time.sleep(2)
confirmDelete = driver.find_element(By.ID, "del")
confirmDelete.click()

time.sleep(2)
logout = driver.find_element(By.CLASS_NAME, "logout")
logout.click()

driver.quit()