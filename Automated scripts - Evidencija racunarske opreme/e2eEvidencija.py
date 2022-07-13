'''Automated test script which creates new piece of equipmet in website section 'Oprema', creates new employee profile
on wesbite section 'Zaposleni' on website 'Evidencija Racunarske Opreme'. The newly registered equipment is then 
assigned to newly created employee. '''

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

movetoEquipment = driver.find_element(By.CSS_SELECTOR, "#wrapper > header > nav > ul:nth-child(1) > li:nth-child(2) > a")
movetoEquipment.click()

time.sleep(2)
typeEquipment = driver.find_element(By.ID, "type_id")
typeEquipment.click()

selectType = driver.find_element(By.CSS_SELECTOR, "#type_id > option:nth-child(4)")
selectType.click()

time.sleep(2)
brandEquipment = driver.find_element(By.ID, "producer_id")
brandEquipment.click()

selectBrand = driver.find_element(By.CSS_SELECTOR, "#producer_id > option:nth-child(14)")
selectBrand.click()

time.sleep(2)
numberInventory = driver.find_element(By.NAME, "inventoryNumber")
numberInventory.send_keys("1001")
numberSerial = driver.find_element(By.NAME, "serialNumber")
numberSerial.send_keys("LMN369")

saveEquipment = driver.find_element(By.NAME, "save")
saveEquipment.click()

time.sleep(2)
movetoEmployees = driver.find_element(By.CSS_SELECTOR, "#wrapper > header > nav > ul:nth-child(1) > li:nth-child(1) > a")
movetoEmployees.click()

time.sleep(2)
firstName = driver.find_element(By.NAME, "firstname")
lastName = driver.find_element(By.NAME, "lastname")
emailAddress = driver.find_element(By.NAME, "email")
phoneNumber = driver.find_element(By.NAME, "phone")

firstName.send_keys("Ana")
lastName.send_keys("Banana")
emailAddress.send_keys("new_employee@banana.com")
phoneNumber.send_keys("+38763453423")

time.sleep(1)
chooseOffice = driver.find_element(By.ID, "office_id")
chooseOffice.click()
selectOffice = driver.find_element(By.CSS_SELECTOR, "#office_id > option:nth-child(12)")
selectOffice.click()

chooseOrgUnit = driver.find_element(By.ID, "organization_id")
chooseOrgUnit.click()
selectOrgUnit = driver.find_element(By.CSS_SELECTOR, "#organization_id > option:nth-child(3)")
selectOrgUnit.click()

time.sleep(2)
saveEmployee = driver.find_element(By.NAME, "save")
saveEmployee.click()

time.sleep(2)
moveNextPage = driver.find_element(By.CLASS_NAME, "btnPage")
moveNextPage.click()

time.sleep(2)
assignEquipment = driver.find_element(By.CSS_SELECTOR, "#results > div > table > tbody > tr:nth-child(3) > td:nth-child(8) > button.button.blue")
assignEquipment.click()

time.sleep(1)
checkEquipment = driver.find_element(By.NAME, "checkEquip")
checkEquipment.click()
saveAssign = driver.find_element(By.NAME, "obligation")
saveAssign.click()

time.sleep(2)
logout = driver.find_element(By.CLASS_NAME, "logout")
logout.click()

driver.quit()