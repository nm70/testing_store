from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebElement

import math

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.__wait = WebDriverWait(browser, 15, 0.3)


    def open(self):
        self.browser.get(self.url)

    def is_present(self, find_by: str, locator: str) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((find_by, locator)))

    def is_text_in_element(self, find_by: str, locator: str, locator_name: str) -> WebElement:
        return self.__wait.until(ec.text_to_be_present_in_element([find_by, locator], locator_name))

    def is_clickable(self, find_by: str, locator: str)-> WebElement:
        return self.__wait.until(ec.element_to_be_clickable((find_by, locator)))

    def find_element(self, find_by: str, locator: str) -> WebElement:
        return self.browser.find_element(By.CSS_SELECTOR(find_by), locator)

    # def is_element_present(self, find_by: str, locator_name: str):
    #     try:
    #         self.__wait.until(ec.presence_of_element_located((find_by, locator_name)))
    #         self.browser.find_element(find_by, locator_name)
    #     except NoSuchElementException:
    #         return False
    #
    #     return True


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
