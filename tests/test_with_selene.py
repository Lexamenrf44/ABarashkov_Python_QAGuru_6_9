import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene import by, be


@allure.label("owner", "abarashkov")
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.story('With allure steps')
def test_github():

    browser.open("/")

    browser.element(".search-input").click()
    browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
    browser.element("#query-builder-test").submit()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#65")).should(be.visible)

    browser.quit()
