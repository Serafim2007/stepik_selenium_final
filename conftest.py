import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if user_language is not None:
        browser_name = request.config.getoption("browser_name")
        if browser_name == "chrome":
            print(f"\nstart chrome browser with language {user_language}")
            browser = webdriver.Chrome()
        elif browser_name == "firefox":
            print(f"\nstart firefox browser with language {user_language}")
            browser = webdriver.Firefox()
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    else:
        raise pytest.UsageError("--Choose language")
    yield browser
    print("\nquit browser..")
    browser.quit()
