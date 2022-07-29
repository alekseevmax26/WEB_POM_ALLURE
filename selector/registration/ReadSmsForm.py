from allure import step
from selenium.webdriver.common.by import By

from selector.authorization.BasePage import BasePage


class LocatorsSms:
    sms = (By.ID, "code")
    confirm_number = (By.ID, "confirm-number")
    wrong_number = (By.ID, "go-back")


class SmsRead(BasePage):

    @step("Ввести смс код")
    def sms(self):
        sms = self.find_element(LocatorsSms.sms)
        sms.clear()
        sms.send_keys()
        return sms

    @step("Подтвердить номер")
    def click_confirm_number(self):
       self.find_element(LocatorsSms.confirm_number).click()

    @step("Не правильный номер")
    def click_wrong_number(self):
        self.find_element(LocatorsSms.wrong_number).click()
