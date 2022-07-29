from allure import title
from selector.authorization.ForgotPasswordByEmailForm import ForgotPasswordByEmail
from selector.authorization.AuthorizationForm import Authorization
from selector.registration.PasswordForm import Password


@title("Восстановление пароля по почте")
def test_resset_password_by_mail(browser, dotenv, get_code, url):
    resset_by_mail = ForgotPasswordByEmail(browser, url)
    resset_by_mail.open(url)
    resset_by_mail.click_forgot_password()
    resset_by_mail.click_by_email()
    auth = Authorization(browser, url)
    auth.enter_mail()
    resset_by_mail.click_confirm_button()
    resset_by_mail.enter_code(get_code)
    resset_by_mail.click_confirm_code()
    passwd = Password(browser, url)
    passwd.enter_password()
    passwd.enter_confirm_password()
    passwd.click_create_password()
    resset_by_mail.click_sign_in()
