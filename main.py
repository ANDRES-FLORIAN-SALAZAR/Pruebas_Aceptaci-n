from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.get("https://demoqa.com/automation-practice-form")
    return driver

def datos_texto_formulario(driver):
    datos: dict[str, str] = {
        "firstName": "Duvan",
        "lastName": "Florian",
        "userEmail": "duvanfloriansalazar@gmail.com",
        "userNumber": "3001234567",
        "currentAddress": "Calle 123 # 45 - 67",
    }

    for campo_id, valor in datos.items():
        driver.find_element(By.ID, campo_id).send_keys(valor)
        time.sleep(1)
        
    subjects = driver.find_element(By.ID, "subjectsInput")
    subjects.send_keys("Maths")
    subjects.send_keys(Keys.ENTER)
    time.sleep(1)

def seleccionar_genero(driver):
    driver.find_element(By.XPATH, "//label[text()='Male']").click()
    time.sleep(0.5)

def seleccionar_hobbies(driver):
    driver.find_element(By.XPATH, "//label[text()='Sports']").click()
    driver.find_element(By.XPATH, "//label[text()='Music']").click()
    time.sleep(0.5)

def seleccionar_fecha_nacimiento(driver):
    driver.find_element(By.ID, "dateOfBirthInput").click()
    time.sleep(0.5)
    driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("April")
    driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("2000")
    driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='15']").click()
    time.sleep(0.5)

def seleccionar_estado_y_ciudad(driver):
    driver.find_element(By.ID, "state").click()
    driver.find_element(By.XPATH, "//div[text()='NCR']").click()
    time.sleep(0.5)
    driver.find_element(By.ID, "city").click()
    driver.find_element(By.XPATH, "//div[text()='Delhi']").click()  # Cambiado a una opción válida real
    time.sleep(0.5)

def main():
    driver = get_driver()
    datos_texto_formulario(driver)
    seleccionar_genero(driver)
    seleccionar_hobbies(driver)
    seleccionar_fecha_nacimiento(driver)
    seleccionar_estado_y_ciudad(driver)
    driver.save_screenshot("antes_de_enviar.png")
    driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    driver.save_screenshot("despues_de_enviar.png")
    driver.quit()

if __name__ == "__main__":
    main()
