from allure import title

from selector.search.Search import Search


@title("Поиск по name&photo_url")
def test_search_name_photo_url(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_name()
    search.click_photo_url_btn()
    search.set_photo_url()
    search.click_search_btn()
    search.check_results_photo_url()
