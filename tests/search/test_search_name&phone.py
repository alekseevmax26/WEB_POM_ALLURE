from allure import title

from selector.search.Search import Search


@title("Поиск по name&phone")
def test_search_name_phone(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_name()
    search.click_phone_btn()
    search.set_phone()
    search.click_search_btn()
    search.check_results_name()
    search.check_results_phone()
