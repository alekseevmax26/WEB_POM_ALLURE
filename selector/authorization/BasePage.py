import logging
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.logger = logging.getLogger(type(self).__name__)

    def open_browser(self):
        self.logger.info("Opening url: {}".format(self.url))
        self.browser.get(self.url)

    def find_element(self, locator, timeout=20):
        # кастомный поиск элемента с ожидаением по существованию элемента

        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise allure.attach(self.browser.get_screenshot_as_png(), name="screenshot",
                                attachment_type=AttachmentType.PNG)
        return element

    def find_element_with_wait_clickable(self, locator, timeout=10):
        # кастомный поиск элемента с ожидаением по существованию элемента

        try:
            element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError("Не найден элемент с селектором: {}".format(locator))
        except ElementNotInteractableException:
            raise allure.attach(self.browser.get_screenshot_as_png(), name="screenshot",
                                attachment_type=AttachmentType.PNG)
        return element

    def click_element(self, locator, timeout=50):
        # кастомный поиск элемента с ожидаением по существованию элемента

        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise allure.attach(self.browser.get_screenshot_as_png(), name="screenshot",
                                attachment_type=AttachmentType.PNG)
        return element

    def find_element_from_search(self, locator, timeout=630):
        # кастомный поиск элемента с ожидаением по существованию элемента

        try:
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise allure.attach(self.browser.get_screenshot_as_png(), name="screenshot",
                                attachment_type=AttachmentType.PNG)
        return element
