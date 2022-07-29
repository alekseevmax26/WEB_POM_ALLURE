from allure import title

from selector.search.Search import Search


@title("Поиск по name&location&education&company&photo")
def test_serach_name_location_educatuin_company_photo(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_name()
    search.set_location()
    search.click_education_btn()
    search.set_education()
    search.click_company_btn()
    search.set_company()
    search.click_photo_btn()
    search.set_upload_photo()
    search.click_search_btn()
    search.check_results_name()
    search.check_results_education()
    search.check_results_company()
    search.check_results_photo()
