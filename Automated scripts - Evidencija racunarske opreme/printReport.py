'''Automated test script that opens up website section 'Izvjestaji' on website 'Evidencija Racunarske Opreme' 
and selects report on offices to be printed. '''

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
movetoReports = driver.find_element(By.CSS_SELECTOR, "#wrapper > header > nav > ul:nth-child(1) > li:nth-child(3) > a")
movetoReports.click()

time.sleep(1)
selectOffice = driver.find_element(By.ID, "office_id")
selectOffice.click()

time.sleep(1)
clickOffice = driver.find_element(By.CSS_SELECTOR, "#office_id > option:nth-child(5)")
clickOffice.click()

time.sleep(2)
printReport = driver.find_element(By.NAME, "officeReport")
printReport.click()

time.sleep(2)
logout = driver.find_element(By.CLASS_NAME, "logout")
logout.click()

driver.quit()
