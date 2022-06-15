from pages.BoardPage import BoardPage
from pages.LandingTrello import TrelloLandingPage
from pages.HomePage import HomePage
from pages.NavBarLanding import NavBarLanding
from pages.common.BaseWrapper import BaseWrapper


class BasePage(BaseWrapper):

    def __init__(self, driver):
        """
            Page initialization.
        """
        super().__init__(driver)
        self.landing_page = TrelloLandingPage(driver)
        self.home_page = HomePage(driver)
        self.navBar_landing = NavBarLanding(driver)
        self.board_page = BoardPage(driver)
