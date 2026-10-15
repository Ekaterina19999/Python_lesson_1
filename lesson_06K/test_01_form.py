from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_fill_form_and_check_validation():
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.maximize_window()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )
        wait = WebDriverWait(driver, 10)

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        submit_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )

        driver.execute_script("arguments[0].click();", submit_btn)

        zip_code_field = wait.until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )

        assert "alert-danger" in zip_code_field.get_attribute("class")

        green_fields_ids = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]

        for field_id in green_fields_ids:
            field_element = driver.find_element(By.ID, field_id)
            assert "alert-success" in field_element.get_attribute("class")

    finally:
        driver.quit()
