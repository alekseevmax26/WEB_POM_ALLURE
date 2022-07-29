import os
from allure import step
from selenium.webdriver.common.by import By
from selector.authorization.BasePage import BasePage


class LocatorAuthorization:
    mail = (By.ID, "email")
    password = (By.ID, "sign-in-password")
    sign_in = (By.ID, "sign-in-btn")
    postfix_url = "/login"


class Authorization(BasePage):
    @step("Открыть ссылку")
    def open(self, url):
        self.browser.get(url + LocatorAuthorization.postfix_url)

    @step("Ввод почты")
    def enter_mail(self):
        self.find_element(LocatorAuthorization.mail).send_keys(os.environ["mail"])

    @step("Ввод пароля")
    def enter_password(self):
        self.find_element(LocatorAuthorization.password).send_keys(os.environ["password"])

    @step("Нажать войти")
    def click_sign_in(self):
        self.find_element(LocatorAuthorization.sign_in).click()

    @step("авторизация")
    def authorization(self, email, password):
        self.find_element(LocatorAuthorization.mail).send_keys(email)
        self.find_element(LocatorAuthorization.password).send_keys(password)
        self.find_element(LocatorAuthorization.sign_in).click()
