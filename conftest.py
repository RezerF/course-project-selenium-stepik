import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help="Choose --browser_name")

    parser.addoption('--language', action='store', default='en', help="Choose --language")




@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    if browser_name == 'Chrome' or browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print('\nstart chrome browser for tests...')
        browser = webdriver.Chrome(options=options)
    else:
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        print('\nstart browser firefox')
        browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print('\nquit browser')
    browser.quit()


