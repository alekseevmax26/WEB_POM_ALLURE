
from allure import title

from selector.search.Search import Search
import time

@title("Поиск по имени и фотографии")
def test_search_name_photo(dotenv, browser, url, authorization):

    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_name()
    search.click_photo_btn()
    search.set_upload_photo()
    time.sleep(5)
    search.click_search_btn()
    search.check_results_name()
    search.check_results_photo()
