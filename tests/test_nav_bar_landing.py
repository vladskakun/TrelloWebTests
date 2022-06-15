"""Test trello Navigation Bar on Landing:"""
import allure
import pytest
from allure_commons.types import Severity

from tests.test_data import nav_bar_landing_test_data


@allure.title("Test trello landing:")
@allure.severity(Severity.NORMAL)
@pytest.mark.parametrize("test_data", nav_bar_landing_test_data.NAV_BAR_DATA)
def test_nav_bar_features_buttons(app, test_data):
    """
        Verify that the user has the ability to open web-site as an unauthorised user.
    """
    btn_name, subbtn_name, expected_result = test_data
    with allure.step("Go to site"):
        app.go_to_site()
        app.navBar_landing.click_navbar_btn(btn_name)
        app.navBar_landing.click_navbar_subbtn(subbtn_name)
        assert expected_result == app.navBar_landing.get_h1_text(), "Button doesn`t same as expected"


