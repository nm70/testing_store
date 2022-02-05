from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    # добавить в корзину
    def click_button_add_to_basket(self):
        self.is_clickable(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    # есть сообщение о том, что товар добавлен в корзину
    def should_be_alert_product_to_basket(self):
        assert self.is_present(*ProductPageLocators.ALERT_PRODUCT_TITLE), 'товар не добавлен в корзину'
        return self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_TITLE)

    # названия товара в сообщении и в корзине совпадают
    def should_be_products_title_is_equal(self):
        el = self.should_be_alert_product_to_basket().text
        assert self.is_text_in_element(*ProductPageLocators.PRODUCT_TITLE, el), "названия товара в сообщении и в корзине не совпадают"

    # есть ообщение со стоимостью корзины
    def should_be_alert_basket_price(self):
        assert self.is_present(*ProductPageLocators.ALERT_PRODUCT_PRICE), 'нет сообщения о стоимости корзины'
        return self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_PRICE)

    # цена товара в сообщении и в корзине совпадают
    def should_be_products_price_is_equal(self):
        el = self.should_be_alert_basket_price().text
        assert self.is_text_in_element(*ProductPageLocators.PRODUCT_PRICE, el), "цена товара в сообщении и в корзине не совпадают"



