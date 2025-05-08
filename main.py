from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

# Casillas de formulario

nombre = driver.find_element(By.ID, "firstName")
nombre.send_keys("duvan")

nombre = driver.find_element(By.ID, "lastName")
nombre.send_keys("Florian")

email = driver.find_element(By.ID, "userEmail")
email.send_keys("duvanfloriansalazar@gmail.com")

mobile = driver.find_element(By.ID, "userNumber")
mobile.send_keys("3001234567")

subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Matematicas")

currentAddress = driver.find_element(By.ID, "currentAddress")
currentAddress.send_keys("Calle 123 # 45 - 67")

sudmit = driver.find_element(By.ID, "submit")
sudmit.submit()


time.sleep(3)
driver.quit()
