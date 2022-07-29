from allure import title

from selector.search.Search import Search


@title("Поиск по alias&phone")
def test_search_alias_phone(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_alias()
    search.click_phone_btn()
    search.set_phone()
    search.click_search_btn()
    search.check_results_alias()
    search.check_results_phone()
