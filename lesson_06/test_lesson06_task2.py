from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

TOKEN_USER_1 = "NzVhODY4N2ItZWYyOS00YjBiLTgzOWYtODQwNzA3NTY4NDcy"
TOKEN_USER_2 = "ODYyZDFmZDAtNjRlOC00ODllLTlhNTMtMTVkNjg4MTA2Nzg4"

URL_PROFILE_USER_1 = "https://gitflic.ru/user/bhgrt"
URL_PROFILE_USER_2 = "https://gitflic.ru/user/ekaro01234"


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    driver.get("https://gitflic.ru")

    cookie_1 = {"name": "token", "value": TOKEN_USER_1, "domain": "gitflic.ru"}
    driver.add_cookie(cookie_1)
    driver.refresh()

    driver.get(URL_PROFILE_USER_1)
    url_user_1 = driver.current_url

    wait.until(EC.presence_of_element_located((By.XPATH, "html")))

    driver.delete_all_cookies()

    cookie_2 = {"name": "token", "value": TOKEN_USER_2, "domain": "gitflic.ru"}
    driver.add_cookie(cookie_2)
    driver.refresh()

    driver.get(URL_PROFILE_USER_2)
    url_user_2 = driver.current_url

    wait.until(EC.presence_of_element_located((By.XPATH, "html")))

    assert url_user_1 != url_user_2, (
        f"Ошибка: URL личных кабинетов совпадают ({url_user_1})."
    )

    driver.quit()


if __name__ == "__main__":
    test_session_storage_auth()
