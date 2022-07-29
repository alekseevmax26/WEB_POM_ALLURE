from datetime import datetime

from selenium.webdriver.common.by import By
from allure import step
from selector.authorization.BasePage import BasePage


class LocatorForgotPasswordByPhone:
    forgot_password = (By.ID, "forgot-password")
    by_phone = (By.ID, "reset-password-by-phone")
    confirm = (By.ID, "reset-password-confirm")
    confirm_code = (By.ID, "reset-password-next")
    sign_in = (By.ID, "back-to-login")
    postfix_url = "/login"
    enter_code = (By.ID, "reset-password-code")


class ForgotPasswordByPhone(BasePage):
    @step("Открыть ссылку")
    def open(self, url):
        self.browser.get(url + LocatorForgotPasswordByPhone.postfix_url)

    @step("Нажать восстановление пароля")
    def click_forgot_password(self):
        self.click_element(LocatorForgotPasswordByPhone.forgot_password).click()

    @step("Нажать 'по телефону' ")
    def click_by_phone(self):
        self.click_element(LocatorForgotPasswordByPhone.by_phone).click()

    @step("Подвердить")
    def click_confirm(self):
        self.click_element(LocatorForgotPasswordByPhone.confirm).click()

    @step("Ввести код")
    def click_confirm_code(self):
        self.click_element(LocatorForgotPasswordByPhone.confirm_code).click()

    @step("Нажать войти")
    def click_sign_in(self):
        self.click_element(LocatorForgotPasswordByPhone.sign_in).click()

    @step("Код телефона")
    def enter_cod(self, get_sms):
        message_sent_after = datetime.utcnow()
        enter_code = self.find_element(LocatorForgotPasswordByPhone.enter_code).send_keys(
            get_sms.read_sms(message_sent_after).split()[-1])
        return enter_code
