import os

import pytest
import logging

from selector.authorization.AuthorizationForm import Authorization
from utils.GetCodeByMail import GetCode
from utils.GetLinkByMail import imap
from utils.twillio import SmsFromTwillio

from selenium import webdriver
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, filename="../selenium.log")
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome')
    parser.addoption('--url', action='store', default=os.environ['url_test'])
    parser.addoption("--headless", action="store", help="Run headless")
    parser.addoption("--executor", action="store", default=os.environ.get('url_test'))
    parser.addoption("--bversion", action="store", default="92.0")
    parser.addoption("--vnc", action="store_true", default=True)


@pytest.fixture(scope="session")
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    headless = request.config.getoption("--headless")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    driver = None
    logger.info(f"Run browser {browser_name}")

    if executor == os.environ['url_test']:
        capabilities = {'goog:chromeOptions': {}}
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument("--window-size=1920,1080")

            if headless:
                options.headless = True
            driver = webdriver.Chrome(options=options, desired_capabilities=capabilities, )
        else:
            executor_url = f"http://{executor}:4444/wd/hub"

            capabilities = {
                "browserName": browser_name,
                "browserVersion": version,
                "name": "test_opencart",
                "selenoid:options": {
                    "sessionTimeout": "60s",
                    "enableVNC": vnc
                }
            }

            driver = webdriver.Remote(
                command_executor=executor_url,
                desired_capabilities=capabilities
            )

        driver.maximize_window()

    def final():
        logger.info(f"Browser {browser_name} close")
        driver.quit()

    request.addfinalizer(final)
    return driver


@pytest.fixture(scope='module')
def get_link():
    return imap()


@pytest.fixture(autouse=True)
def dotenv():
    return load_dotenv()


@pytest.fixture(scope='session')
def get_sms():
    return SmsFromTwillio()


@pytest.fixture(scope="session")
def get_code():
    return GetCode()


@pytest.fixture()
def authorization(browser, url):
    email = os.environ["mail"]
    password = os.environ["password"]
    browser.get(url)
    auth = Authorization(browser, url)
    auth.authorization(email, password)
    return authorization
