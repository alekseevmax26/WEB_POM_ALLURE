from allure import title

from selector.search.Search import Search


@title("Поиск по alias&email&phone")
def test_search_alias_email_phone(dotenv, browser, url, authorization):
    search = Search(browser, url)
    search.open_case()
    search.open_new_search()
    search.set_alias()
    search.click_email_btn()
    search.set_email()
    search.click_phone_btn()
    search.set_phone()
    search.click_search_btn()
    search.check_results_alias()
    search.check_results_email()
    search.check_results_phone()
