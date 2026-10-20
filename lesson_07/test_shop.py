import pytest
from selenium import webdriver
from shop_pages import LoginPage, ProductsPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_checkout_flow(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
    products_page.add_product_to_cart("Sauce Labs Onesie")
    products_page.go_to_cart()

    cart_page.click_checkout()

    checkout_page.fill_checkout_form("Иван", "Петров", "123456")

    total_price = checkout_page.get_total_price()

    assert "Total: $58.29" in total_price, (
        f"Ожидалась сумма $58.29, но на странице: {total_price}"
    )
