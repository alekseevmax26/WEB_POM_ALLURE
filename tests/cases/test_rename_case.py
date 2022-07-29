from allure import title

from selector.search.Search import Search
from selector.cases.CaseForm import Cases


@title("Переименование кейса")
def test_rename_case(dotenv, browser, url, authorization):
    case = Cases(browser, url)
    case.click_rename_case()
    case.click_case_name()
    case.click_accept_case_name()
    search = Search(browser, url)
    search.open_case()
