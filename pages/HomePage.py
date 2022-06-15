from pages.common.BaseWrapper import BaseWrapper
from pages.elements.ButtonElement import ButtonElement
from pages.elements.InputElement import InputElement


class HomePage(BaseWrapper):
    """
        Locators and methods for landing page.
    """

    NAVBAR_USER_BTN_XPATH = "//button[@aria-label='Открыть меню участников']"
    CREATE_BOARD_BTN_XPATH = "//div[@class='board-tile mod-add']"
    BOARD_NAME_INP_XPATH = "//input[@data-test-id='create-board-title-input']"
    CREATE_BOARD_SUBMIT_BTN_XPATH = "//button[@data-test-id='create-board-submit-button']"
    TEST_BOARD_XPATH = "//div[@title='Test Board']"
    BOARDS_SECTION_XPATH = "//ul[@class='boards-page-board-section-list']/li"
    BOARDS_BTN_XPATH = "//a[@href='/testuservladskakun/boards']"
    WORKSPACES_BTN_XPATH = "//button[@aria-label='Рабочие пространства']"
    SECTION_HEADER_MENU_XPATH = "//section//li//span"
    LOGOUT_BTN_XPATH = "//button[@id='logout-submit']"
    EXIT_ATLASSIAN = "//h5"

    def __init__(self, driver):
        super().__init__(driver)
        self.navbar_user_btn = ButtonElement(self.NAVBAR_USER_BTN_XPATH, driver)
        self.boards_btn = ButtonElement(self.BOARDS_BTN_XPATH, driver)
        self.board_name_inp = InputElement(self.BOARD_NAME_INP_XPATH, driver)
        self.create_board_subm_btn = ButtonElement(self.CREATE_BOARD_SUBMIT_BTN_XPATH, driver)
        self.test_board_btn = ButtonElement(self.TEST_BOARD_XPATH, driver)
        self.workspace_btn = ButtonElement(self.WORKSPACES_BTN_XPATH, driver)
        self.create_board_btn = ButtonElement(self.CREATE_BOARD_BTN_XPATH, driver)
        self.logout_btn = ButtonElement(self.LOGOUT_BTN_XPATH, driver)

    def click_section_header_menu_btn(self, btn_name):
        """
            Method for click checkboxes in 'More filters' menu depending on text value.
            param btn_name: It's parameter to select needed button.
        """
        elements = self.find_elements_by_xpath(self.SECTION_HEADER_MENU_XPATH)
        for element in elements:
            if btn_name in element.text:
                element.click()
                return

    def get_boards_button_text(self):
        """
            Method for getting the text with boards button.
        """
        return self.find_element_by_xpath(self.BOARDS_BTN_XPATH).text

    def get_exit_atlassian_text(self):
        """
            Method for getting the text with exit atlassian lable.
        """
        return self.find_element_by_xpath(self.EXIT_ATLASSIAN).text

    def get_quantity_boards(self):
        """
            Method for return quantity boards.
        """
        return len(self.find_elements_by_xpath(self.BOARDS_SECTION_XPATH))
