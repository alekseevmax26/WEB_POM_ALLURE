from allure import title

from selector.search.Search import Search


@title("Поиск по name&education")
def test_search_name_education(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_name()
    search.click_education_btn()
    search.set_education()
    search.click_search_btn()
    search.check_results_education()
