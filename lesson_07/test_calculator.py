import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()

    calc_page.set_delay("45")

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    result_text = calc_page.get_result(timeout=50)

    assert result_text == "15", (
        f"Ожидался результат 15, но калькулятор показал: {result_text}"
    )
