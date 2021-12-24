from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    # перейдите на страницу входа
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.ID, "login_link")
        login_link.click()

    # должна быть ссылка для входа
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"