from allure import title

from selector.registration.NamePhoneForm import NamePhone
from selector.registration.ReadSmsForm import SmsRead
from selector.registration.CompanyForm import CompanyData
from selector.registration.PasswordForm import Password


@title("Не верный телефон")
def test_wrong_phone_registration(browser, dotenv, get_sms, get_link, url):
    enter_name_phone = NamePhone(browser, url)
    enter_name_phone.open(url)
    enter_name_phone.enter_name()
    enter_name_phone.enter_surname()
    enter_name_phone.enter_wrong_number()
    enter_name_phone.click_button()
    enter_sms = SmsRead(browser, url)
    enter_sms.click_wrong_number()
    enter_name_phone.enter_phone()
    enter_name_phone.click_button()
    enter_name_phone.enter_cod(get_sms)
    enter_sms.click_confirm_number()
    company = CompanyData(browser, url)
    company.enter_company_name()
    company.enter_role_in_company()
    company.enter_your_business_email()
    company.click_submit()
    browser.get(get_link.get_link_for_mail())
    passwd = Password(browser, url)
    passwd.enter_password()
    passwd.enter_confirm_password()
    passwd.click_create_password()
