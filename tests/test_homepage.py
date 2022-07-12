import time
import pytest

from pages.home_page import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        time.sleep(2)
        homepage_nav.click_on_links()
