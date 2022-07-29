from allure import title

from selector.search.Search import Search


@title("Поиск по name&company")
def test_search_name_company(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_name()
    search.click_company_btn()
    search.set_company()
    search.click_search_btn()
    search.check_results_company()
