"""Test trello home page:"""
import allure
from allure_commons.types import Severity
from tests.test_data import section_header_menu_data as section_data


@allure.title("Test Log Out:")
@allure.severity(Severity.NORMAL)
def test_landing_logout(authorised_setup):
    """
         Verify that user has the ability to log out.
    """
    expected_result = "Log In"
    with allure.step("click header menu"):
        authorised_setup.home_page.navbar_user_btn.click_btn_by_xpath()
    with allure.step("Click Log Out Button on header menu"):
        authorised_setup.home_page.click_section_header_menu_btn(section_data.LOGOUT)
    with allure.step("Click Log Out Button"):
        authorised_setup.home_page.logout_btn.click_btn_by_xpath()
    with allure.step("Verify logout"):
        assert expected_result == authorised_setup.landing_page.get_login_button_text(), \
            "Button text doesn`t same as expected"
