"""Test trello landing:"""
import allure
from allure_commons.types import Severity


@allure.title("Test trello landing:")
@allure.severity(Severity.CRITICAL)
def test_landing_check(app):
    """
        Verify that the user has the ability to open web-site as an unauthorised user.
    """
    expected_result = "Log In"
    with allure.step("Go to site"):
        app.landing_page.go_to_site()
    with allure.step("Verify it was landing page in unautorize state"):
        assert expected_result == app.landing_page.get_login_button_text(), "Button doesn`t same as expected"


@allure.title("Test login:")
@allure.severity(Severity.BLOCKER)
def test_landing_login(authorised_setup):
    """
         Verify that user has the ability to login in as an Admin.
    """
    expected_result = "Доски"
    with allure.step("Verify username is as expected"):
        assert expected_result == authorised_setup.home_page.get_boards_button_text(), \
            "username results doesn`t same as expected"
