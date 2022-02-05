
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options

# передача параметров из командной строки в pytest для настройки тестового окружения
def pytest_addoption(parser):
    # браузер
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose browser: chrome or firefox")
    # язык
    parser.addoption('--language', default='en')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    #обработчик, который считывает из командной строки параметр language
    user_language = request.config.getoption('language')
    # если хром
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = chrome_options()
        #браузер с указанным языком пользователя
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")


    yield browser
    print("\nquit browser..")
    browser.quit()


