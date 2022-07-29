from allure import title

from selector.search.Search import Search


@title("Поиск по имени и локации")
def test_search_name_location(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_name()
    search.set_location()
    search.click_search_btn()
    search.check_results_name()
