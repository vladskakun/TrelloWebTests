from pages.common.BaseWrapper import BaseWrapper


class ButtonElements(BaseWrapper):
    """
        Class for click on Button by text button.
    """
    def __init__(self, selector, driver):
        super().__init__(driver)
        self.selector = selector

    def click_btn_by_name_by_css(self, btn_name):
        """
            Method for click on a needed button by text button and css selector.
        """
        elements = self.find_elements(self.selector)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return

    def click_btn_by_name_by_xpath(self, btn_name):
        """
            Method for click on a needed button by text button and xpath.
        """
        elements = self.find_elements_by_xpath(self.selector)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return
