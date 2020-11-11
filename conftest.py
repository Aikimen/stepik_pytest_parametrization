import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# класс Options и метод add_experimental_option, используются для
# указания языка браузера в WebDriver

def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default=None,
                     help='Choose language: es, gb, ru and etc...'
                     )
    
    parser.addoption('--browser_name',
                     action='store',
                     default='chrome', # по умолчанию запустится Chrome
                     help='Choose browser: chrome or firefox'
                     )
    
@pytest.fixture(scope='function')
def browser(request):
    # Добавим логику обработки командной строки в conftest.py.
    # Для запроса значения параметра мы можем вызвать команду:
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        # для задания языкового параметра в Google Chrome
        options = Options()
        options.add_experimental_option('prefs',{'intl.accept_languages': user_language})
        print('\nstart browser for test..')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        # для задания языкового параметра в Firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError('--browser name should be chrome or firefox')
    yield browser
    time.sleep(30)
    print('\nquit browser..')
    browser.quit()

