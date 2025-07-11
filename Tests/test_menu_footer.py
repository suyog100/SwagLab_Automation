import pytest

from Locators.alllocators import LoginPageLocators, ProductPageLocators
from Pages.LoginPage import LoginPage
from Pages.OtherPage import OtherPage
from Pages.ProductPage import ProductPage


@pytest.fixture()
def open_product_page(driver):
    login_page = LoginPage(driver)
    login_page.login(LoginPageLocators.valid_username, LoginPageLocators.valid_password)
    product_page = ProductPage(driver)
    product_page.add_single_item(ProductPageLocators.add_back_pack_path)
    menu =OtherPage(driver)
    return menu
@pytest.mark.menu_test
def test_menu_visibility(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    assert menu.is_menu_sidebar_displayed() == True,"Menu bar not displayed"

@pytest.mark.menu_test
def test_menu_cancel(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    menu.click_menu_cancel()
    assert menu.is_menu_sidebar_displayed(),"Menu bar is still displayed,Menu cancel button didnt work"
@pytest.mark.menu_test
def test_click_all_item(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    menu.go_to_all_item()
    assert "inventory" in menu.get_current_url(),f"Didnt go to inventory Page.Got url:{menu.get_current_url()}"
@pytest.mark.menu_test
def test_about_redirect(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    menu.go_to_about()
    assert "saucelabs.com" in menu.get_current_url(),f"Not directed to about page.Directed to {menu.get_current_url()}"
@pytest.mark.menu_test
def test_click_reset_item(open_product_page):
    menu = open_product_page
    #initial_count=1
    menu.click_menu_button()
    menu.reset_app_state()
    menu.click_menu_cancel()
    assert menu.get_cart_count()==0,f"cart was not reset. got{menu.get_cart_count()}"

    #assert menu.get_cart_count()==initial_count,f"cart was reset. got{menu.get_cart_count()}"


@pytest.mark.menu_test
def test_logout(open_product_page):
    menu = open_product_page
    menu.click_menu_button()
    menu.logout()
    assert menu.get_current_url() == LoginPageLocators.loginpageUrl,f"Shoul be in Login page{LoginPageLocators.loginpageUrl} but got url:{menu.get_current_url()}"
@pytest.mark.footer_test
def test_footer_visibility(open_product_page):
    footer = open_product_page
    assert footer.is_footer_displayed(),"Footer bar not displayed"
@pytest.mark.footer_test
def test_footer_twitter(open_product_page):
    footer = open_product_page
    footer.click_twitter_logo()
    assert "x.com/saucelabs" in footer.get_current_url(),f"Twitter site is not displayed,Got url:{footer.get_current_url()}"
@pytest.mark.footer_test
def test_footer_facebook(open_product_page):
    footer = open_product_page
    footer.click_facebook_logo()
    assert "facebook.com" in footer.get_current_url(),f"Facebook site is not displayed, Got url:{footer.get_current_url()}"
@pytest.mark.footer_test
def test_footer_linkedin(open_product_page):
    footer = open_product_page
    footer.click_linkedin_logo()
    assert "linkedin.com" in footer.get_current_url(),f"Linkedin site is not displayed,Got url:{footer.get_current_url()}"




