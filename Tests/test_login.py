import pytest
import time
from Locators.alllocators import LoginPageLocators
from Pages.LoginPage import LoginPage
from Utils.FileReader import load_csv_data


@pytest.mark.parametrize("username,password,expected", load_csv_data("Data/login_data.csv"))
def test_login(driver,username, password, expected):
    login_page = LoginPage(driver)
    assert login_page.get_url()== LoginPageLocators.loginpageUrl
    assert login_page.are_elements_displayed()== True
    login_page.login(username, password)
    time.sleep(3)
    if expected=="success":
        assert login_page.get_url() == "https://www.saucedemo.com/inventory.html"
        assert login_page.get_title()== "Swag Labs"
    else:
        assert "Epic sadface" in login_page.get_error_message()

