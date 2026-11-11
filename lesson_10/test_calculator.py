import pytest
import allure
from selenium import webdriver
from lesson_10.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка работы медленного калькулятора")
@allure.description(
    "Тест проверяет сложение чисел 7 и 8 с учетом установленной задержки."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver) -> None:
    calc_page = CalculatorPage(driver)

    calc_page.open()
    calc_page.set_delay("45")

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    result_text = calc_page.get_result(timeout=50)

    with allure.step("Проверить, что итоговый результат на экране равен '15'"):
        assert result_text == "15", (
            f"Ожидался результат 15, но калькулятор показал: {result_text}"
        )
