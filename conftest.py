import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if user_language != None:
        print(f"\nstart chrome browser with language {user_language}")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--Choose language")
    yield browser
    print("\nquit browser..")
    browser.quit()
