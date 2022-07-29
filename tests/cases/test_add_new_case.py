from allure import title

from selector.search.Search import Search
from selector.cases.CaseForm import Cases


@title("Создание нового кейса")
def test_add_new_case(dotenv, browser, url, authorization):
    case = Cases(browser, url)
    case.click_add_new_case()
    search = Search(browser, url)
    search.set_name()
    search.click_search_btn()
    search.check_results_name()
