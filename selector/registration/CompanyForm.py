import os
from allure import step
from selenium.webdriver.common.by import By

from selector.authorization.BasePage import BasePage


class SelectorCompany:
    company_name = (By.ID, "company")
    role_in_company = (By.ID, "role")
    your_business_email = (By.ID, "email")
    submit = (By.ID, "company-info-form-submit")
    wrong_email = (By.ID, "email")
    back_to_company_info = (By.ID, "back-to-company-info")
    postfix_url = "/registration"


class CompanyData(BasePage):
    @step("Открыть ссылку")
    def open(self, url):
        self.browser.get(url + SelectorCompany.postfix_url)

    @step("Имя компании")
    def enter_company_name(self):
        self.find_element(SelectorCompany.company_name).send_keys('QWERTY')

    @step("Роль в компании")
    def enter_role_in_company(self):
        self.find_element(SelectorCompany.role_in_company).send_keys('QWERTY')

    @step("Бизнес почта")
    def enter_your_business_email(self):
        your_business_email = self.find_element(SelectorCompany.your_business_email)
        your_business_email.clear()
        your_business_email.send_keys(os.environ['mail'])

    @step("Подтвердить")
    def click_submit(self):
        self.click_element(SelectorCompany.submit).click()

    @step("Не правильный пароль")
    def wrong_email(self):
        self.find_element(SelectorCompany.wrong_email).send_keys(os.environ['wrong_email'])

    @step("Вернуться")
    def back_to_company(self):
        self.click_element(SelectorCompany.back_to_company_info).click()
