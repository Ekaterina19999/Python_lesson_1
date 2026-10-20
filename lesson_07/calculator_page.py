from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
        self.RESULT_SCREEN = (By.CSS_SELECTOR, "div.screen")
        self.BUTTON_XPATH = "//span[text()='{}']"

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, seconds: str):
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, button_text: str):
        xpath = self.BUTTON_XPATH.format(button_text)
        self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self, timeout: int) -> str:
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, "15")
        )
        return self.driver.find_element(*self.RESULT_SCREEN).text
