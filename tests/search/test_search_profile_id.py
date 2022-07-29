from allure import title

from selector.search.Search import Search


@title("Поиск по profile_id")
def test_search_profile_id(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.click_profile_url_btn()
    search.set_profile_url()
    search.click_search_btn()
    search.check_results_profile_id()
