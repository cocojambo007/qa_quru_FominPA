from selene.support.shared import browser
from selene import be, have
from input_data import POSITIVE, NEGATIVE


def test_positive(browser_setup):
    browser.element('[name="q"]').should(be.blank).type(POSITIVE).press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_negative(browser_setup):
    browser.element('[name="q"]').should(be.blank).type(NEGATIVE).press_enter()
    browser.element('[id="topstuff"]').should(have.text(f'По запросу {NEGATIVE} ничего не найдено.'))
