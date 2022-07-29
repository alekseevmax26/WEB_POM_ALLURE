import os
from allure import step
from selenium.webdriver.common.by import By

from selector.authorization.BasePage import BasePage


class SelectorPassword:
    password = (By.ID, "password")
    confirm_password = (By.ID, "confirm")
    create_password = (By.ID, "create-password")


class Password(BasePage):

    @step("Ввести пароль")
    def enter_password(self):
        self.find_element(SelectorPassword.password).send_keys(os.environ['password'])

    @step("Подтвердить пароль")
    def enter_confirm_password(self):
        self.find_element(SelectorPassword.confirm_password).send_keys(os.environ['password'])

    @step("Создать пароль")
    def click_create_password(self):
        self.find_element(SelectorPassword.create_password).click()
