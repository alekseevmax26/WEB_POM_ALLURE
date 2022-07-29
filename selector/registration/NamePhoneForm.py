import os
from datetime import datetime

import names
from allure import step
from selenium.webdriver.common.by import By

from selector.authorization.BasePage import BasePage


class LocatorsNamePhone:
    name = (By.ID, "reg-name")
    surname = (By.ID, "reg-surname")
    phone = (By.ID, "phone")
    next_step = (By.ID, "reg-next-step")
    postfix_url = "/registration"
    enter_code = (By.ID, "code")


class NamePhone(BasePage):
    @step("Открыть ссылку")
    def open(self, url):
        self.browser.get(url + LocatorsNamePhone.postfix_url)

    @step("Ввести имя")
    def enter_name(self):
        name = self.find_element(LocatorsNamePhone.name).send_keys(names.get_first_name())
        return name

    @step("Ввести фамилию")
    def enter_surname(self):
        surname = self.find_element(LocatorsNamePhone.surname).send_keys(names.get_last_name())
        return surname

    @step("Ввести телефон")
    def enter_phone(self):
        phone = self.find_element(LocatorsNamePhone.phone)
        phone.clear()
        phone.send_keys(os.environ['phone'])
        return phone

    @step("Подтвердить")
    def click_button(self):
        self.find_element(LocatorsNamePhone.next_step).click()

    @step("Нажать на неправельный пароль")
    def enter_wrong_number(self):
        self.find_element(LocatorsNamePhone.phone).send_keys(os.environ['wrong_phone'])

    @step("Код телефона")
    def enter_cod(self, get_sms):
        message_sent_after = datetime.utcnow()
        enter_code = self.find_element(LocatorsNamePhone.enter_code).send_keys(
            get_sms.read_sms(message_sent_after).split()[-1])
        return enter_code
