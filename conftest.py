import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import allure
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.saucedemo.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    print('start')
    yield driver
    driver.quit()
    print('finish')


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    marker = item.get_closest_marker("ui")
    if marker:
        if rep.when == "call" and rep.failed:
            try:
                allure.attach(item.instance.driver.get_screenshot_as_png(),
                              name=item.name,
                              attachment_type=allure.attachment_type.PNG)
            except Exception as e:
                print(e)
