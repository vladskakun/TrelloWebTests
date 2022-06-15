import time

from pages.common.BaseWrapper import BaseWrapper
from pages.elements.ButtonElement import ButtonElement
from pages.elements.InputElement import InputElement


class LandingPage(BaseWrapper):
    """
        Locators and methods for landing page.
    """

    SIGN_IN_UP_BTN_XPATH = "//a[@href='/login']/span"
    FORM_EMAIL_INP_XPATH = "//div/input[@name='user']"
    FORM_PASSWORD_INP_XPATH = "//div/input[@name='password']"
    LOG_IN_BUTTON_XPATH = "//button[@id='login-submit']"
    LOGIN_WITH_ATLASSIAN_XPATH = "//input[@id='login']"

    def __init__(self, driver):
        super().__init__(driver)
        self.sign_up_btn = ButtonElement(self.SIGN_IN_UP_BTN_XPATH, driver)
        self.email_inp = InputElement(self.FORM_EMAIL_INP_XPATH, driver)
        self.pass_inp = InputElement(self.FORM_PASSWORD_INP_XPATH, driver)
        self.log_in_btn = ButtonElement(self.LOG_IN_BUTTON_XPATH, driver)
        self.login_with_atlassian = ButtonElement(self.LOGIN_WITH_ATLASSIAN_XPATH, driver)

    def get_login_button_text(self):
        """
            Method for getting the message with login button.
        """
        return self.find_element_by_xpath(self.SIGN_IN_UP_BTN_XPATH).text

    def login(self, username, password):
        """
        Sign in method as a scenario
        actor - is a person with own permissions (admin or user).
        :param username: username
        :param password: pass phrase
        """
        self.email_inp.send_data_by_xpath(username)
        self.login_with_atlassian.click_btn_by_xpath()
        # need wait for animation on the website
        time.sleep(3)
        self.pass_inp.send_data_by_xpath(password)
        self.log_in_btn.click_btn_by_xpath()
