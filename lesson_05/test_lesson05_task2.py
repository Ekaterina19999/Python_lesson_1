import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        base_url = "https://httpbin.qa-territory.online/forms/post"
        driver.get(base_url)
        name_input = driver.find_element(By.NAME, "custname")
        name_input.send_keys("Алексей")
        submit_button = driver.find_element(
            By.XPATH, "//button[contains(text(), 'Submit')]"
        )
        submit_button.click()
        for _ in range(50):
            if driver.current_url != base_url:
                break
            time.sleep(0.1)
        assert driver.current_url != base_url, (
            f"URL не изменился после отправки формы и остался {base_url}"
        )
    finally:
        driver.quit()
