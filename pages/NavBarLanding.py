from pages.common.BaseWrapper import BaseWrapper


class NavBarLanding(BaseWrapper):
    """
        Locators and methods for landing page.
    """
    NAVBAR_BTNS_XPATH = "//div[@class='Tabsstyles__TabGroup-sc-1grh34k-2 hniXih']//button"
    NAVBAR_SUBBTN_XPATH = "//div/p[@class='UiNavLinkstyles__NavLinkTitle-sc-lgpipn-3 hPXyna']"
    H1_PATH = "//h1"

    def __init__(self, driver):
        super().__init__(driver)

    def click_navbar_btn(self, btn_name):
        """
            Method for click checkboxes in 'More filters' menu depending on text value.
            param btn_name: It's parameter to select needed button.
        """
        elements = self.find_elements_by_xpath(self.NAVBAR_BTNS_XPATH)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return

    def click_navbar_subbtn(self, btn_name):
        """
            Method for click checkboxes in 'More filters' menu depending on text value.
            :param btn_name: It's parameter to select needed button.
        """
        elements = self.find_elements_by_xpath(self.NAVBAR_SUBBTN_XPATH)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return

    def get_h1_text(self):
        """
            Method for getting text with H1 size object.
        """
        return self.find_element_by_xpath(self.H1_PATH).text
