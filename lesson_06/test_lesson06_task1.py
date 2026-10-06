from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_loading():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    wait = WebDriverWait(driver, 15)

    start_button = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#start > button"))
    )
    start_button.click()

    finish_element = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    driver.save_screenshot("screenshot.png")
    actual_text = finish_element.text

    assert (
        actual_text == "Hello World!"
    ), f"Ожидался текст 'Hello World!', но пришел '{actual_text}'"

    driver.quit()


if __name__ == "__main__":
    test_dynamic_loading()

