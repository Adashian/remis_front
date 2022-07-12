import time

from base.selenium_base import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from base.utils import Utils


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '.menu>li'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Navigation links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return ",".join(nav_links_text)

    def click_on_links(self):
        nav_links = self.get_nav_links()
        for link in nav_links:
            link.click()
            print(link)
            time.sleep(1)
