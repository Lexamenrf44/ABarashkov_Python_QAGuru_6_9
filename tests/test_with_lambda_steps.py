import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene import by, be


@allure.label("owner", "abarashkov")
@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.story('With allure steps')
def test_github():

    with allure.step("Should open main GitHub page"):
        browser.open("/")

    with allure.step("Should navigate to eroshenkoam/allure-example"):
        browser.element(".search-input").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example")
        browser.element("#query-builder-test").submit()

    with allure.step("Should click on the repo link"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Should open Issues"):
        browser.element("#issues-tab").click()

    with allure.step("Should check Issue number #65"):
        browser.element(by.partial_text("#65")).should(be.visible)

    with allure.step("Should close browser"):
        browser.quit()
