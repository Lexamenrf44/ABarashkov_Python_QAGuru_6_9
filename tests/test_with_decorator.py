import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene import by


@allure.label("owner", "abarashkov")
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.story('With decorators')
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number('#65')
    closing_browser()


@allure.step("Should open main GitHub page")
def open_main_page():
    browser.open("/")


@allure.step("Should navigate to {repo}")
def search_for_repository(repo):
    browser.element(".search-input").click()
    browser.element("#query-builder-test").send_keys(repo)
    browser.element("#query-builder-test").submit()


@allure.step("Should click on the repo link")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Should open Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Should check Issue number {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).click()


@allure.step("Should close browser")
def closing_browser():
    browser.quit()
