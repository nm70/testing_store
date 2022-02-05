from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    # перейдите на страницу входа
    def go_to_login_page(self):
        self.is_clickable(*MainPageLocators.LOGIN_LINK)
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    # должна быть ссылка для входа
    def should_be_login_link(self):
        assert self.is_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"