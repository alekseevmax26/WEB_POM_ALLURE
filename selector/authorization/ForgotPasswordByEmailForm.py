from selenium.webdriver.common.by import By
from allure import step
from selector.authorization.BasePage import BasePage


class LocatorForgotPasswordByMail:
    forgot_password = (By.ID, "forgot-password")
    by_email = (By.ID, "reset-password-by-email")
    confirm = (By.CSS_SELECTOR, ".confirm-buttons__confirm")
    enter_code = (By.ID, "reset-password-code")
    confirm_code = (By.ID, "reset-password-next")
    sign_in = (By.ID, "back-to-login")
    postfix_url = "/login"


class ForgotPasswordByEmail(BasePage):
    @step("Открыть ссылку")
    def open(self, url):
        self.browser.get(url + LocatorForgotPasswordByMail.postfix_url)

    @step("Нажать 'востановление пароля'")
    def click_forgot_password(self):
        self.find_element_with_wait_clickable(LocatorForgotPasswordByMail.forgot_password).click()

    @step("Нажать 'по почте'")
    def click_by_email(self):
        self.find_element_with_wait_clickable(LocatorForgotPasswordByMail.by_email).click()

    @step("Нажать подвтвердить")
    def click_confirm_button(self):
        self.find_element_with_wait_clickable(LocatorForgotPasswordByMail.confirm).click()

    @step("Ввести код")
    def enter_code(self, get_code):
        enter_code = self.find_element(LocatorForgotPasswordByMail.enter_code).send_keys(get_code.get_code_for_mail())
        return enter_code

    @step("Нажать подтвердить")
    def click_confirm_code(self):
        self.find_element_with_wait_clickable(LocatorForgotPasswordByMail.confirm_code).click()

    @step("Нажать войти")
    def click_sign_in(self):
        self.find_element_with_wait_clickable(LocatorForgotPasswordByMail.sign_in).click()
