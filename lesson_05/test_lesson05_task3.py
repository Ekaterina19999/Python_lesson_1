from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    try:
        # Открываем строго правильный URL из задания
        driver.get("https://httpbin.qa-territory.online/links/10")

        links = driver.find_elements(By.TAG_NAME, "a")
        assert len(links) == 9, (
            f"Ожидалось 9 ссылок, но обнаружено {len(links)}"
        )

        for index, link in enumerate(links):
            assert link.is_displayed(), (
                f"Ссылка с индексом {index} не отображается"
            )
        first_link_text = links[0].text
        assert "1" in first_link_text, (
            f"Текст первой ссылки должен содержать '1', "
            f"но получили '{first_link_text}'"
        )
    finally:
        driver.quit()
