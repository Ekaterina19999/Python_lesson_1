from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://saucedemo.com"
        self.USERNAME_INPUT = (By.CSS_SELECTOR, "#user-name")
        self.PASSWORD_INPUT = (By.CSS_SELECTOR, "#password")
        self.LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class ProductsPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link")
        self.ADD_TO_CART_XPATH = (
            "//div[text()='{}']/ancestor::"
            "div[@class='inventory_item_description']//button"
        )

    def add_product_to_cart(self, product_name: str):
        xpath = self.ADD_TO_CART_XPATH.format(product_name)
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()


class CartPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkout")

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()


class CheckoutPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
        self.LAST_NAME = (By.CSS_SELECTOR, "#last-name")
        self.POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
        self.CONTINUE_BUTTON = (By.CSS_SELECTOR, "#continue")
        self.TOTAL_LABEL = (By.CSS_SELECTOR, "div.summary_total_label")

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total_price(self) -> str:
        return self.driver.find_element(*self.TOTAL_LABEL).text
