"""Test for board page:"""
import allure
import pytest
from allure_commons.types import Severity
from tests.test_data import create_board_data as board_data

COLUMN_NAME = "New column"
NEW_COLUMN_NAME = "Updated column"


@allure.title("Test Create Board:")
@allure.severity(Severity.NORMAL)
def test_create_board(authorised_setup):
    expected_result = board_data.BOARD_NAME
    with allure.step("Click create board button"):
        authorised_setup.home_page.create_board_btn.click_btn_by_xpath()
    with allure.step("Input board name"):
        authorised_setup.home_page.board_name_inp.send_data_by_xpath(board_data.BOARD_NAME)
    with allure.step("Create board"):
        authorised_setup.home_page.create_board_subm_btn.click_btn_by_xpath()
    assert expected_result == authorised_setup.board_page.get_board_name_text(), "Board name not equal as expected"


@allure.title("Test add new column to the Board:")
@allure.severity(Severity.NORMAL)
def test_add_column(authorised_setup):
    expected_result = 4
    with allure.step("Open board"):
        authorised_setup.home_page.test_board_btn.click_btn_by_xpath()
    with allure.step("Click add new column"):
        authorised_setup.board_page.add_new_column_btn.click_btn_by_xpath()
    with allure.step("Write name column"):
        authorised_setup.board_page.column_name_inp.send_data_by_xpath(COLUMN_NAME)
    with allure.step("Click add column"):
        authorised_setup.board_page.add_new_column_subm_btn.click_btn_by_xpath()
    with allure.step("Assert quantity"):
        assert expected_result == authorised_setup.board_page.get_quantity_boards(), "Column name not equal as expected"


@pytest.mark.skip("Skip test")
@allure.title("Test rename created column on the Board:")
@allure.severity(Severity.MINOR)
def test_rename_column(authorised_setup):
    expected_result = NEW_COLUMN_NAME
    with allure.step("Open board"):
        authorised_setup.home_page.test_board_btn.click_btn_by_xpath()
    with allure.step("Click on column name"):
        authorised_setup.board_page.click_and_send_on_input(NEW_COLUMN_NAME)
    with allure.step("Assert new column name"):
        assert expected_result == authorised_setup.board_page.get_column_name_text(), \
            "Column name not equal as expected"


@allure.title("Test delete created column on the Board:")
@allure.severity(Severity.NORMAL)
def test_delete_column(authorised_setup):
    expected_result = 3
    with allure.step("Open board"):
        authorised_setup.home_page.test_board_btn.click_btn_by_xpath()
    with allure.step("Open details"):
        authorised_setup.board_page.menu_column_btn.click_btn_by_xpath()
    with allure.step("Delete column"):
        authorised_setup.board_page.delete_column_menu_btn.click_btn_by_xpath()
    with allure.step("Assert quantity"):
        assert expected_result == authorised_setup.board_page.get_quantity_boards()


@allure.title("Test Delete Board:")
@allure.severity(Severity.NORMAL)
def test_delete_board(authorised_setup):
    expected_result = 1
    with allure.step("Open created board"):
        authorised_setup.home_page.test_board_btn.click_btn_by_xpath()
    with allure.step("Click Menu Button"):
        authorised_setup.board_page.menu_btn.click_btn_by_xpath()
    with allure.step("Click More Button"):
        authorised_setup.board_page.menu_more.click_btn_by_xpath()
    with allure.step("Click Close Board Button"):
        authorised_setup.board_page.close_board_btn.click_btn_by_xpath()
    with allure.step("Click Submit Close Board Button"):
        authorised_setup.board_page.close_board_submit_btn.click_btn_by_xpath()
    with allure.step("Click forever delete"):
        authorised_setup.board_page.delete_board_forever_btn.click_btn_by_xpath()
    with allure.step("Click Submit forever delete"):
        authorised_setup.board_page.submit_delete_board_forever_btn.click_btn_by_xpath()
    with allure.step("Assert thet board is deleted"):
        assert expected_result == authorised_setup.home_page.get_quantity_boards()
