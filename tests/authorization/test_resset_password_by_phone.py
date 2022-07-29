from allure import title
from selector.authorization.ForgotPasswordByPhoneForm import ForgotPasswordByPhone
from selector.registration.NamePhoneForm import NamePhone
from selector.registration.PasswordForm import Password


@title("Востановление пароля по номеру телефона")
def test_reset_password_by_phone(browser, get_sms, url):
    resset_by_phone = ForgotPasswordByPhone(browser, url)
    resset_by_phone.open(url)
    resset_by_phone.click_forgot_password()
    resset_by_phone.click_by_phone()
    auth = NamePhone(browser, url)
    auth.enter_phone()
    resset_by_phone.click_confirm()
    resset_by_phone.enter_cod(get_sms)
    resset_by_phone.click_confirm_code()
    passwd = Password(browser, url)
    passwd.enter_password()
    passwd.enter_confirm_password()
    passwd.click_create_password()
    resset_by_phone.click_sign_in()
