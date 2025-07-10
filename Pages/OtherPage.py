
from Locators.alllocators import OtherPageLocators
from Pages.BasePage import BasePage



class OtherPage(BasePage):
    def get_current_url(self):
        return self.driver.current_url

    def click_menu_button(self):
        self.click_element(OtherPageLocators.menu_button_path)
    def go_to_all_item(self):
        self.click_element(OtherPageLocators.all_item_path)
    def go_to_about(self):
        self.click_element(OtherPageLocators.about_path)
    def logout(self):
        self.click_element(OtherPageLocators.logout_path)
    def reset_app_state(self):
        self.click_element(OtherPageLocators.reset_app_state_path)
    def click_menu_cancel(self):
        self.click_element(OtherPageLocators.menu_close_path)
    def is_menu_sidebar_displayed(self):
        return self.is_displayed(OtherPageLocators.menu_container_path)
    def is_footer_displayed(self):
        return self.is_displayed(OtherPageLocators.footer_path)

    def click_twitter_logo(self):
        self.click_element(OtherPageLocators.twitter_path)
    def click_facebook_logo(self):
        self.click_element(OtherPageLocators.facebook_path)
    def click_linkedin_logo(self):
        self.click_element(OtherPageLocators.linkedin_path)

