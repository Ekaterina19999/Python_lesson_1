import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс для работы со страницей медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CalculatorPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.url: str = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.DELAY_INPUT: tuple[str, str] = (By.CSS_SELECTOR, "#delay")
        self.RESULT_SCREEN: tuple[str, str] = (By.CSS_SELECTOR, "div.screen")
        self.BUTTON_XPATH: str = "//span[text()='{}']"

    @allure.step("Открыть страницу калькулятора")
    def open(self) -> None:
        """Открывает веб-страницу калькулятора."""
        self.driver.get(self.url)

    @allure.step("Установить задержку {seconds} сек.")
    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает значение задержки в секундах.

        :param seconds: str — строка с количеством секунд.
        """
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(seconds)

    @allure.step("Нажать кнопку '{button_text}'")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает кнопку калькулятора по её тексту.

        :param button_text: str — текст на кнопке.
        """
        xpath = self.BUTTON_XPATH.format(button_text)
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Ожидать и получить результат с экрана калькулятора")
    def get_result(self, timeout: int) -> str:
        """
        Ожидает появления результата и возвращает текст с экрана калькулятора.

        :param timeout: int — время ожидания в секундах.
        :return: str — итоговый текст с экрана.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, "15")
        )
        return self.driver.find_element(*self.RESULT_SCREEN).text
