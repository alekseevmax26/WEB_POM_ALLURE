from allure import step

from selenium.webdriver.common.by import By
from selector.authorization.BasePage import BasePage


class SelectorsCase:
    add_new_case = (By.ID, 'sidebar-add-case')
    rename_case = (By.CSS_SELECTOR, '.case:nth-child(2) .case-edit-panel path')
    delete_case = (By.CLASS_NAME, 'delete-case')
    case_name = (By.CSS_SELECTOR, '.case-name')
    accept_case_name = (By.CLASS_NAME, 'case-editing-ok')
    accept_delete_case = (By.CSS_SELECTOR, '.primary-btn')
    postfix_url = "/login"
    search_btn = (By.ID, "search-btn")
    back_to_case = (By.ID, "main-back")


class Cases(BasePage):
    @step("Открыть ссылку")
    def open(self, url):
        self.browser.get(url + SelectorsCase.postfix_url)

    @step("Добавить новый кейс")
    def click_add_new_case(self):
        self.click_element(SelectorsCase.add_new_case).click()

    @step("Отображение search_btn")
    def search_btn(self):
        self.find_element(SelectorsCase.search_btn)

    @step("Переименовать кейс")
    def click_rename_case(self):
        self.click_element(SelectorsCase.rename_case).click()

    @step("Удалить кейс")
    def click_delete_case(self):
        self.click_element(SelectorsCase.delete_case).click()

    @step("Нажать на имя кейса")
    def click_case_name(self):
        self.find_element(SelectorsCase.case_name).send_keys('Auto test')

    @step("Применить переименование")
    def click_accept_case_name(self):
        self.click_element(SelectorsCase.accept_case_name).click()

    @step("Применить удаление")
    def click_accept_delete_case(self):
        self.click_element(SelectorsCase.accept_delete_case).click()

    @step("Нажать back to case")
    def back_to_case(self):
        self.click_element(SelectorsCase.back_to_case).click()
