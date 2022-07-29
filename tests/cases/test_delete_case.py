from allure import title
from selector.cases.CaseForm import Cases


@title("Удаление кейса")
def test_delete_case(dotenv, browser, url, authorization):
    case = Cases(browser, url)
    case.click_delete_case()
    case.click_accept_delete_case()
