'''Automated script that creates new employee profile on section 'Zaposleni - Zaduzivanje i razduzivanje' on
website 'Evidencija Racunarske Opreme' and assigns new piece of equipment to said profile. '''

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

time.sleep(3)
employeeName = driver.find_element(By.CSS_SELECTOR, "#wrapper > main > section.section-one > div.section-one-left > form > input[type=text]:nth-child(2)")
employeeLastName = driver.find_element(By.CSS_SELECTOR, "#wrapper > main > section.section-one > div.section-one-left > form > input[type=text]:nth-child(3)")
employeeEmail = driver.find_element(By.CSS_SELECTOR, "#wrapper > main > section.section-one > div.section-one-left > form > input[type=text]:nth-child(4)")
employeeNumber = driver.find_element(By.CSS_SELECTOR, "#wrapper > main > section.section-one > div.section-one-left > form > input[type=text]:nth-child(5)")

employeeName.send_keys("AnaTest")
employeeLastName.send_keys("BuljanTest")
employeeEmail.send_keys("ana.buljan@test.com")
employeeNumber.send_keys("00387123123")

time.sleep(2)
officeDrop = driver.find_element(By.ID, "office_id")
officeDrop.click()

officeSelect = driver.find_element(By.CSS_SELECTOR, "#office_id > option:nth-child(3)")
officeSelect.click()

organizationDrop = driver.find_element(By.ID, "organization_id")
organizationDrop.click()

organizationSelect = driver.find_element(By.CSS_SELECTOR, "#organization_id > option:nth-child(5)")
organizationSelect.click()

saveEmployee = driver.find_element(By.CSS_SELECTOR, "#wrapper > main > section.section-one > div.section-one-left > form > input.button.blue")
saveEmployee.click()

time.sleep(2)
newPage = driver.find_element(By.CLASS_NAME, "btnPage")
newPage.click()

time.sleep(2)
assignButton = driver.find_element(By.CSS_SELECTOR, "#results > div > table > tbody > tr:nth-child(8) > td:nth-child(8) > button.button.blue")
assignButton.click()

time.sleep(2)
assignEquipment = driver.find_element(By.NAME, "checkEquip")
assignEquipment.click()

time.sleep(2)
confirmAssign = driver.find_element(By.NAME, "obligation")
confirmAssign.click()

time.sleep(2)
logout = driver.find_element(By.CLASS_NAME, "logout")
logout.click()

driver.quit()