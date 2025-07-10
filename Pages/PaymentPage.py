from Locators.alllocators import ProductPageLocators, CheckoutPageLocators, OtherPageLocators, PaymentPageLocators
from Pages.BasePage import BasePage

class PaymentPage(BasePage):
    def payment_title(self):
        return self.find_element(PaymentPageLocators.payment_title).text

    def check_items(self):

    def check_payment_info(self):

    def check_shipping_info(self):

    def check_cart_total(self):


    def click_cancel_button(self):
        self.click_element(PaymentPageLocators.cancel_button_path)

    def click_finish_button(self):
        self.click_element(PaymentPageLocators.finish_button_path)


