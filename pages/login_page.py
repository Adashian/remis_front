from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class LoginPage(SeleniumBase):
    EMAIL_INPUT = '#email'
    PASSWORD_INPUT = '#password'
    LOGIN_BUTTON = '#root > div.page-layout > div > div.preview-wrap > div > div > form > button'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_nav_links(self, locator) -> WebElement:
        return self.is_visible('css', locator, 'Navigation links')

    def get_nav_links_text(self) -> str:
        email = self.get_nav_links(self.EMAIL_INPUT)
        password = self.get_nav_links(self.PASSWORD_INPUT)
        input_button = self.get_nav_links(self.LOGIN_BUTTON)

        return f'{email}, {password}, {input_button}'

    def auth_user(self):
        email = self.is_visible('css', self.EMAIL_INPUT, 'Navigation links')
        password = self.is_visible('css', self.PASSWORD_INPUT, 'Navigation links')
        login_button = self.is_visible('css', self.LOGIN_BUTTON, 'Navigation links')

        email.send_keys("login")
        password.send_keys("password")
        login_button.click()
