from allure import title

from selector.search.Search import Search


@title("Поиск по name&location&education&company")
def test_search_name_location_education_company(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_name()
    search.set_location()
    search.click_education_btn()
    search.set_education()
    search.click_company_btn()
    search.set_company()
    search.click_search_btn()
    search.check_results_name()
    search.check_results_education()
    search.check_results_company()
