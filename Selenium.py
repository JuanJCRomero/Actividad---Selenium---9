from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

# Configuración del WebDriver
service = Service("chromedriver.exe")  # Asegúrate de que el driver esté en tu PATH
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def login(username, password):
    """Función para iniciar sesión en SauceDemo."""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

class TestSauceDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configura el WebDriver antes de ejecutar las pruebas."""
        cls.driver = webdriver.Chrome(service=service, options=options)
        cls.driver.maximize_window()
    
    def test_login_success(self):
        """Caso de prueba: Inicio de sesión exitoso con credenciales válidas."""
        login("standard_user", "secret_sauce")
        self.assertTrue(WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        ))
    
    def test_login_fail(self):
        """Caso de prueba: Inicio de sesión fallido con credenciales incorrectas."""
        login("invalid_user", "wrong_password")
        error_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        self.assertIn("Epic sadface", error_message)
    
    def test_add_product_to_cart(self):
        """Caso de prueba: Agregar un producto al carrito y verificar que se muestra correctamente."""
        login("standard_user", "secret_sauce")
        product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))
        )
        product.click()
        cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_badge.text, "1")
    
    def test_remove_product_from_cart(self):
        """Caso de prueba: Eliminar un producto del carrito y confirmar que se elimina."""
        login("standard_user", "secret_sauce")
        product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))
        )
        product.click()
        remove_button = self.driver.find_element(By.CLASS_NAME, "btn_secondary")
        remove_button.click()
        cart_badge = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(len(cart_badge), 0)
    
    def test_checkout_process(self):
        """Caso de prueba: Finalizar una compra con datos válidos."""
        login("standard_user", "secret_sauce")
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")
        self.driver.find_element(By.ID, "continue").click()
        self.driver.find_element(By.ID, "finish").click()
        confirmation = self.driver.find_element(By.CLASS_NAME, "complete-header").text
        self.assertEqual(confirmation, "Thank you for your order!")
    
    @classmethod
    def tearDownClass(cls):
        """Cierra el navegador después de ejecutar las pruebas."""
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
