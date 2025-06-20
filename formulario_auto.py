from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Ruta del ChromeDriver
driver_path = r"C:\chromedriver\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Abrir el formulario
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
time.sleep(2)

# Llenar nombre y apellido
driver.find_element(By.NAME, "firstname").send_keys("Santiago")
driver.find_element(By.NAME, "lastname").send_keys("Quiroz")

# Seleccionar género (Male)
driver.find_element(By.ID, "sex-0").click()

# Seleccionar experiencia (5-7 años)
driver.find_element(By.ID, "exp-4").click()

# Ingresar fecha
driver.find_element(By.ID, "datepicker").send_keys("06/19/2025")

# Seleccionar profesiones (Automation Tester)
checkbox = driver.find_element(By.ID, "profession-1")
driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
time.sleep(1)
checkbox.click()

# Seleccionar herramienta (Selenium Webdriver)
driver.find_element(By.ID, "tool-2").click()

# Seleccionar continente (South America)
from selenium.webdriver.support.ui import Select
continente = Select(driver.find_element(By.ID, "continents"))
continente.select_by_visible_text("South America")

# Seleccionar comando de Selenium (Browser Commands)
comando = Select(driver.find_element(By.ID, "selenium_commands"))
comando.select_by_visible_text("Browser Commands")

# Esperar 5 segundos para ver todo antes de cerrar
time.sleep(5)
driver.quit()