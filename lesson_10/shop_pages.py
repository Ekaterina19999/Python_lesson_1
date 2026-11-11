import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс для работы со страницей авторизации магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса LoginPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.url: str = "https://saucedemo.com"
        self.USERNAME_INPUT: tuple[str, str] = (By.CSS_SELECTOR, "#user-name")
        self.PASSWORD_INPUT: tuple[str, str] = (By.CSS_SELECTOR, "#password")
        self.LOGIN_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, "#login-button")

    @allure.step("Открыть страницу авторизации магазина")
    def open(self) -> None:
        """Открывает главную страницу магазина."""
        self.driver.get(self.url)

    @allure.step("Авторизоваться под пользователем '{username}'")
    def login(self, username: str, password: str) -> None:
        """
        Заполняет форму авторизации и нажимает кнопку входа.

        :param username: str — логин пользователя.
        :param password: str — пароль пользователя.
        """
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()


class ProductsPage:
    """Класс для работы со страницей каталога товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса ProductsPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.CART_LINK: tuple[str, str] = (
            By.CSS_SELECTOR, "a.shopping_cart_link"
        )
        self.ADD_TO_CART_XPATH: str = (
            "//div[text()='{}']/ancestor::"
            "div[@class='inventory_item_description']//button"
        )

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_product_to_cart(self, product_name: str) -> None:
        """
        Находит кнопку добавления конкретного товара и нажимает её.

        :param product_name: str — точное название товара.
        """
        xpath = self.ADD_TO_CART_XPATH.format(product_name)
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """Нажимает на иконку перехода в корзину."""
        self.driver.find_element(*self.CART_LINK).click()


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CartPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.CHECKOUT_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, "#checkout")

    @allure.step("Нажать кнопку 'Checkout'")
    def click_checkout(self) -> None:
        """Нажимает на кнопку оформления заказа."""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Конструктор класса CheckoutPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.FIRST_NAME: tuple[str, str] = (By.CSS_SELECTOR, "#first-name")
        self.LAST_NAME: tuple[str, str] = (By.CSS_SELECTOR, "#last-name")
        self.POSTAL_CODE: tuple[str, str] = (By.CSS_SELECTOR, "#postal-code")
        self.CONTINUE_BUTTON: tuple[str, str] = (By.CSS_SELECTOR, "#continue")
        self.TOTAL_LABEL: tuple[str, str] = (
            By.CSS_SELECTOR, "div.summary_total_label"
        )

    @allure.step(
        "Заполнить форму оформления заказа: "
        "{first_name} {last_name}, индекс: {postal_code}"
    )
    def fill_checkout_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет персональные данные покупателя и нажимает 'Continue'.

        :param first_name: str — имя.
        :param last_name: str — фамилия.
        :param postal_code: str — почтовый индекс.
        """
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    @allure.step("Получить итоговую стоимость заказа")
    def get_total_price(self) -> str:
        """
        Возвращает текстовое значение общей суммы заказа.

        :return: str — строка с итоговой стоимостью.
        """
        return self.driver.find_element(*self.TOTAL_LABEL).text
