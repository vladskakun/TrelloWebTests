import time

import config
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseWrapper:

    def __init__(self, driver):
        """
            Method for class fields declaration.
        """
        self.driver = driver
        self.base_url = config.BASE_URL

    def find_element_by_css(self, locator, timeout=10):
        """
            Method for search element by css selector with wait
        """
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)),
                                                  message=f"Can't find element by locator {locator}")
        element = self.driver.find_element(By.CSS_SELECTOR, locator)
        return element

    def find_element_by_xpath(self, locator, timeout=10):
        """
            Method for search element by xpath selector with wait
        """
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)),
                                                  message=f"Can't find element by locator {locator}")
        element = self.driver.find_element(By.XPATH, locator)
        return element

    def find_elements(self, locator, timeout=10):
        """
            Method for search elements by css selector with wait
        """
        WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)),
                                                  message=f"Can't find elements by locator {locator}")
        elements = self.driver.find_elements(By.CSS_SELECTOR, locator)
        return elements

    def find_elements_by_xpath(self, locator, timeout=10):
        """
            Method for search elements by xpath selector with wait
        """
        time.sleep(1)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, locator)),
                                                  message=f"Can't find elements by locator {locator}")
        elements = self.driver.find_elements(By.XPATH, locator)
        return elements

    def go_to_site(self):
        """
            Method for go to the base_url
        """
        site = self.driver.get(config.BASE_URL)
        return site
