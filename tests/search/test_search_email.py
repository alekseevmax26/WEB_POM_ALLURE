from allure import title

from selector.search.Search import Search


@title("Поиск по email")
def test_search_email(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.click_email_btn()
    search.set_email()
    search.click_search_btn()
    search.check_results_email()
