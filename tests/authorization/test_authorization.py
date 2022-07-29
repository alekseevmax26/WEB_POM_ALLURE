from allure import title
from selector.authorization.AuthorizationForm import Authorization


@title("Тест авторизации")
def test_authorization(dotenv, browser, url):
    auth = Authorization(browser, url)
    auth.open_browser()
    auth.enter_mail()
    auth.enter_password()
    auth.click_sign_in()
