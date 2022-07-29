from allure import title

from selector.registration.NamePhoneForm import NamePhone
from selector.registration.ReadSmsForm import SmsRead
from selector.registration.CompanyForm import CompanyData
from selector.registration.PasswordForm import Password


@title("Не корректная почта")
def test_wrong_mail(browser, dotenv, get_sms, get_link, url):
    inter_name_phone = NamePhone(browser, url)
    inter_name_phone.open(url)
    inter_name_phone.enter_name()
    inter_name_phone.enter_surname()
    inter_name_phone.enter_phone()
    inter_name_phone.click_button()
    inter_name_phone.enter_cod(get_sms)
    inter_sms = SmsRead(browser, url)
    inter_sms.click_confirm_number()
    company = CompanyData(browser, url)
    company.enter_company_name()
    company.enter_role_in_company()
    company.wrong_email()
    company.click_submit()
    company.back_to_company()
    company.enter_your_business_email()
    company.click_submit()
    browser.get(get_link.get_link_for_mail())
    passw = Password(browser, url)
    passw.enter_password()
    passw.enter_confirm_password()
    passw.click_create_password()
