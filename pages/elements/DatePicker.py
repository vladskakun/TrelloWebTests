from pages.common.BaseWrapper import BaseWrapper
from selenium.webdriver.common.keys import Keys


class DatePicker(BaseWrapper):
    """
        Class for send DatePickers by css selector.
    """
    def __init__(self, selector, driver):
        super().__init__(driver)
        self.selector = selector

    def write_date_to_datepicker_by_css(self, day, month, year):
        """
            Method for write date on a datepicker by css selector.
            Day, month, year - are integer values.
        """
        element = self.find_element_by_css(self.selector)
        element.send_keys(year)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(month)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(day)

    def write_date_to_datepicker_by_xpath(self, day, month, year):
        """
            Method for write date on a datepicker by xpath.
            Day, month, year - are integer values.
        """
        element = self.find_element_by_xpath(self.selector)
        element.send_keys(year)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(month)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(Keys.ARROW_LEFT)
        element.send_keys(day)

    def get_datepicker_text_by_css(self):
        """
            Returns value from datepicker field by css selector.
        """
        return self.find_element_by_css(self.selector).text

    def get_datepicker_text_by_xpath(self):
        """
            Returns value from datepicker field by css selector.
        """
        return self.find_element_by_css(self.selector).text
