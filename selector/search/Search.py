import os

from allure import step
from selenium.webdriver.common.by import By

from selector.authorization.BasePage import BasePage


class SelectorSearch:
    open_case = (By.CSS_SELECTOR, ".case:nth-child(2) .typography-3")
    open_new_search = (By.CSS_SELECTOR, ".right-icon")
    name = (By.ID, "name")
    location = (By.ID, "location")
    education_btn = (By.ID, "education-btn")
    education = (By.ID, "education")
    company_btn = (By.ID, "company-btn")
    company = (By.ID, "company")
    alias = (By.ID, "username")
    photo_btn = (By.ID, "photo-btn")
    upload_photo = (By.ID, "upload-photo")
    photo_url_btn = (By.ID, "photo-url-btn")
    photo_url = (By.ID, "photo-url")
    profile_url_btn = (By.ID, "profile-url-btn")
    profile_url = (By.ID, "profile-url")
    profile_id_btn = (By.ID, "profile-id-btn")
    profile_id = (By.ID, "profile-id")
    phone_btn = (By.ID, "phone-btn")
    phone = (By.ID, "phone-input")
    email_btn = (By.ID, "email-btn")
    email = (By.ID, "email")
    search_btn = (By.ID, "search-btn")
    results_name = (By.XPATH, "//div[@id='layout']/main/div/div/div[3]/div[3]/header/div")
    results_education = (By.CSS_SELECTOR, ".search-group-header:nth-child(1) > .search-type")
    results_company = (By.CSS_SELECTOR, ".search-group-header:nth-child(3) button")
    results_alias = (By.XPATH, "//div[3]/header/div")
    results_photo = (By.CSS_SELECTOR, ".search-group-header:nth-child(1) > .search-type")
    results_photo_url = (By.CSS_SELECTOR, ".search-group-header:nth-child(1) > .search-type")
    results_phone = (By.XPATH, "//div[@id='layout']/main/div/div/div[3]/div[3]/header/div")
    results_email = (By.XPATH, "//div[3]/header/div")
    results_profile_url = (By.CSS_SELECTOR, ".profile-card__photo")
    results_profile_id = (By.CSS_SELECTOR, ".profile-card__photo")


class Search(BasePage):
    @step("Открыть кейс")
    def open_case(self):
        self.click_element(SelectorSearch.open_case).click()

    @step("Открыть новый поиск")
    def open_new_search(self):
        self.click_element(SelectorSearch.open_new_search).click()

    @step("Ввод имени")
    def set_name(self):
        self.find_element(SelectorSearch.name).send_keys("")

    @step("Ввод локации")
    def set_location(self):
        self.find_element(SelectorSearch.location).send_keys("")

    @step("Нажать кнопку education")
    def click_education_btn(self):
        self.click_element(SelectorSearch.education_btn).click()

    @step("Ввод education")
    def set_education(self):
        self.find_element(SelectorSearch.education).send_keys("")

    @step("Нажать кнопку company")
    def click_company_btn(self):
        self.click_element(SelectorSearch.company_btn).click()

    @step("Ввод company")
    def set_company(self):
        self.find_element(SelectorSearch.company).send_keys("")

    @step("Ввод alias")
    def set_alias(self):
        self.find_element(SelectorSearch.alias).send_keys("")

    @step("Нажать photo")
    def click_photo_btn(self):
        self.click_element(SelectorSearch.photo_btn).click()

    @step("Добавить photo")
    def set_upload_photo(self):
        self.find_element(SelectorSearch.upload_photo).send_keys("")

    @step("Нажать photo_url_btn")
    def click_photo_url_btn(self):
        self.click_element(SelectorSearch.photo_url_btn).click()

    @step("Ввести photo_url")
    def set_photo_url(self):
        self.find_element(SelectorSearch.photo_url).send_keys(
            "")

    @step("Нажать profile_id_btn")
    def click_profile_id_btn(self):
        self.click_element(SelectorSearch.profile_id_btn).click()

    @step("Ввести profile_id")
    def set_profile_id(self):
        self.find_element(SelectorSearch.profile_id).send_keys("")

    @step("Нажать profile_url_btn")
    def click_profile_url_btn(self):
        self.click_element(SelectorSearch.profile_url_btn).click()

    @step("Ввести profile_url")
    def set_profile_url(self):
        self.find_element(SelectorSearch.profile_url).send_keys(
            "")

    @step("Нажать phone_btn")
    def click_phone_btn(self):
        self.click_element(SelectorSearch.phone_btn).click()

    @step("Ввести phone")
    def set_phone(self):
        self.find_element(SelectorSearch.phone).send_keys("")

    @step("Нажать email_btn")
    def click_email_btn(self):
        self.click_element(SelectorSearch.email_btn).click()

    @step("Ввести email")
    def set_email(self):
        self.find_element(SelectorSearch.email).send_keys("")

    @step("Нажать search_btn")
    def click_search_btn(self):
        self.click_element(SelectorSearch.search_btn).click()

    @step("Ожидание show_on_overview")
    def check_results_name(self):
        self.find_element_from_search(SelectorSearch.results_name)

    @step("Ожидание результата поиска по education")
    def check_results_education(self):
        self.find_element_from_search(SelectorSearch.results_education)

    @step("Ожидание результата поиска по company")
    def check_results_company(self):
        self.find_element_from_search(SelectorSearch.results_company)

    @step("Ожидание поиска по alias")
    def check_results_alias(self):
        self.find_element_from_search(SelectorSearch.results_alias)

    @step("Ожидание поиски по photo")
    def check_results_photo(self):
        self.find_element_from_search(SelectorSearch.results_photo)

    @step("Ожидание поиска по photo_url")
    def check_results_photo_url(self):
        self.find_element_from_search(SelectorSearch.results_photo_url)

    @step("Ожидание поиска по phone")
    def check_results_phone(self):
        self.find_element_from_search(SelectorSearch.results_phone)

    @step("Ожидание поиска по email")
    def check_results_email(self):
        self.find_element_from_search(SelectorSearch.results_email)

    @step("Ожидание поиски по url_profile")
    def check_results_profile_url(self):
        self.find_element_from_search(SelectorSearch.results_profile_url)

    @step("Ожидание поиски по url_profile")
    def check_results_profile_id(self):
        self.find_element_from_search(SelectorSearch.results_profile_id)
