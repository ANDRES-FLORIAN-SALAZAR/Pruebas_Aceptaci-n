from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

# Casillas de formulario

# nombre = driver.find_element(By.ID, "firstName")
# nombre.send_keys("duvan")

# nombre = driver.find_element(By.ID, "lastName")
# nombre.send_keys("Florian")

# email = driver.find_element(By.ID, "userEmail")
# email.send_keys("duvanfloriansalazar@gmail.com")

# mobile = driver.find_element(By.ID, "userNumber")
# mobile.send_keys("3001234567")

# subjects = driver.find_element(By.ID, "subjectsInput")
# subjects.send_keys("Matematicas")

# currentAddress = driver.find_element(By.ID, "currentAddress")
# currentAddress.send_keys("Calle 123 # 45 - 67")

# sudmit = driver.find_element(By.ID, "submit")
# sudmit.submit()

def get_driver():
    
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    options.add_argument("--incognito")
    
    driver = webdriver.Chrome(options)
    driver.get("https://demoqa.com/automation-practice-form")
    return driver

def datos_texto_formulario(driver):
    datos : dict[str,str] = {
            "firstName": "duvan",
            "lastName": "Florian",
            "userEmail": "duvanfloriansalazar@gmail.com",
            "userNumber": "3001234567",
            "subjectsInput": "Matematicas",
            "currentAddress": "Calle 123 # 45 - 67",
            "submit": "submit"
}
    
    for id_pag in datos:
        texto: str = datos[id_pag]
        driver.find_element(By.ID, id_pag).send_keys(texto)
        time.sleep(3)
        
def main():
    driver: webdriver = get_driver()
    datos_texto_formulario(driver)
    driver.save_screenshot("Antes_de_enviar.png")
    driver.find_element(By.ID, "submit").submit()
    driver.save_screenshot("despues_de_enviar.png")

    time.sleep(2)
    driver.quit()
    
if __name__ == "__main__":
    main()
