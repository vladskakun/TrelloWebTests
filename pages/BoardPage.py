import time

from selenium.webdriver import Keys

from pages.common.BaseWrapper import BaseWrapper
from pages.elements.ButtonElement import ButtonElement
from pages.elements.InputElement import InputElement


class BoardPage(BaseWrapper):
    """
        Locators and methods for landing page.
    """

    NAME_BOARD_XPATH = "//h1"
    MENU_BTN_XPATH = "//a[contains(@class,'mod-show-menu')]/span[@class='board-header-btn-text']"
    MENU_MORE_BTN_XPATH = "//a[contains(@class,'js-open-more')]"
    CLOSE_BOARD_BTN_XPATH = "//a[contains(@class,'js-close-board')]"
    CLOSE_BOARD_SUBMIT_BTN_XPATH = "//input[contains(@class,'nch-button--danger')]"
    DELETE_BOARD_FOREVER_BTN_XPATH = "//button[@data-test-id='close-board-delete-board-button']"
    SUBMIT_DELETE_BOARD_FOREVER_BTN_XPATH = "//button[@data-test-id='close-board-delete-board-confirm-button']"

    LISTS_ON_BOARD_XPATH = "//div[@class='list js-list-content']"
    ADD_NEW_COLUMN_XPATH = "//a[@class='open-add-list js-open-add-list']"
    COLUMN_NAME_INP_XPATH = "//input[@class='list-name-input']"
    ADD_NEW_COLUMN_SUBMIT_XPATH = "//input[contains(@class,'js-save-edit')]"

    RENAME_COLUMN_XPATH = "(//div/div[contains(@class,'js-editing-target')])[last()]"
    INPUT_RENAME_COLUMN_XPATH = "//textarea[contains(@class,'is-editing')]"
    NEW_NAME_COLUMN_XPATH = "(//div/textarea)[last()]"

    MENU_COLUMN_XPATH = "(//div/a[contains(@class,'icon-overflow-menu-horizontal')])[last()]"
    DELETE_COLUMN_MENU_OPTION_XPATH = "//li/a[@class='js-close-list']"

    def __init__(self, driver):
        super().__init__(driver)
        self.menu_btn = ButtonElement(self.MENU_BTN_XPATH, driver)
        self.menu_more = ButtonElement(self.MENU_MORE_BTN_XPATH, driver)
        self.close_board_btn = ButtonElement(self.CLOSE_BOARD_BTN_XPATH, driver)
        self.close_board_submit_btn = ButtonElement(self.CLOSE_BOARD_SUBMIT_BTN_XPATH, driver)
        self.delete_board_forever_btn = ButtonElement(self.DELETE_BOARD_FOREVER_BTN_XPATH, driver)
        self.submit_delete_board_forever_btn = ButtonElement(self.SUBMIT_DELETE_BOARD_FOREVER_BTN_XPATH, driver)
        self.add_new_column_btn = ButtonElement(self.ADD_NEW_COLUMN_XPATH, driver)
        self.column_name_inp = InputElement(self.COLUMN_NAME_INP_XPATH, driver)
        self.add_new_column_subm_btn = ButtonElement(self.ADD_NEW_COLUMN_SUBMIT_XPATH, driver)
        self.menu_column_btn = ButtonElement(self.MENU_COLUMN_XPATH, driver)
        self.delete_column_menu_btn = ButtonElement(self.DELETE_COLUMN_MENU_OPTION_XPATH, driver)

    def get_board_name_text(self):
        """
            Method for getting the text with login button.
        """
        return self.find_element_by_xpath(self.NAME_BOARD_XPATH).text

    def get_column_name_text(self):
        time.sleep(5)
        return self.find_element_by_xpath(self.NEW_NAME_COLUMN_XPATH).text

    def click_and_send_on_input(self, new_name):
        element = self.find_element_by_xpath(self.RENAME_COLUMN_XPATH)
        element.click()
        element = self.find_element_by_xpath(self.INPUT_RENAME_COLUMN_XPATH)
        element.send_keys(new_name)
        element.send_keys(Keys.ENTER)

    def get_quantity_boards(self):
        time.sleep(1)
        return len(self.find_elements_by_xpath(self.LISTS_ON_BOARD_XPATH))
