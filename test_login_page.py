from .pages.login_page import LoginPage

# тест должны видеть страницу логина
def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
