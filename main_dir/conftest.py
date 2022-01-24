import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help='Выберите браузер, Chrome или Firefox')

@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome' or browser_name == 'Chrome':
        browser = webdriver.Chrome()
    elif browser_name == 'firefox' or browser_name == 'Firefox':
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError ('--browser_name доллжен быть Firefox или Chrome')
    yield browser
    browser.quit()