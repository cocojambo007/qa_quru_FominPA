from selene import browser, be, have, by
import os

FIRSTNAME = 'Павел'
LASTNAME = 'Фомин'
EMAIL = 'test@test.ru'
MOBILE = '8800555353'
FILE = 'Screenshot_1.jpg'
ADDRESS = 'Current Address'
STATE = 'Uttar Pradesh'
CITY = 'Agra'


def test_les5(browser_setup):
    browser.element(by.id('firstName')).should(be.blank).type(FIRSTNAME)  # поле first name
    browser.element(by.id('lastName')).should(be.blank).type(LASTNAME)  # поле last name
    browser.element(by.id('userEmail')).should(be.blank).type(EMAIL)  # поле email
    browser.element('div[class*="custom-control"] label[for="gender-radio-1"]').click()  # выбор gender
    browser.element(by.id('userNumber')).should(be.blank).type(MOBILE)  # поле телефон
    browser.element(by.id('dateOfBirthInput')).click()  # выбор поля день рождения
    browser.element('select[class="react-datepicker__month-select"] option[value="6"]').click()  # выбор месяца
    browser.element('select[class="react-datepicker__year-select"] option[value="1993"]').click()  # выбор года
    browser.element('div[class="react-datepicker__day react-datepicker__day--005"]').click()  # выбор даты
    browser.element(by.id('subjectsInput')).should(be.blank).type('Maths').press_enter()  # поле subject
    browser.element('div[class="custom-control custom-checkbox custom-control-inline"] label[for="hobbies-checkbox-1"]') \
        .click()  # выбор хобби
    browser.element(by.id('uploadPicture')).send_keys(os.getcwd() + f'/resources/{FILE}')  # загрузка файла
    browser.element(by.id('currentAddress')).should(be.blank).type(ADDRESS).click()  # поле адреса
    browser.element(by.id('react-select-3-input')).type(STATE).press_enter()  # выбор state
    browser.element(by.id('react-select-4-input')).type(CITY).press_enter()  # выбор city
    browser.element(by.id('submit')).click()  # нажатие кнопки submit
    '''Проверки полей на валидность'''
    browser.element(by.id('example-modal-sizes-title-lg')).should(
        have.text('Thanks for submitting the form'))  # проверка всплывающего окна
    browser.element('tr:nth-child(1) td:nth-child(2)').should(
        have.text(f'{FIRSTNAME} {LASTNAME}'))  # проверка поля Student Name
    browser.element('tr:nth-child(2) td:nth-child(2)').should(have.text(EMAIL))  # проверка поля Student Email
    browser.element('tr:nth-child(3) td:nth-child(2)').should(have.text('Male'))  # проверка поля Gender
    browser.element('tr:nth-child(4) td:nth-child(2)').should(have.text(MOBILE))  # проверка поля Mobile
    browser.element('tr:nth-child(5) td:nth-child(2)').should(have.text('05 July,1993'))  # проверка поля Date of Birth
    browser.element('tr:nth-child(6) td:nth-child(2)').should(have.text('Maths'))  # проверка поля Subjects
    browser.element('tr:nth-child(7) td:nth-child(2)').should(have.text('Sports'))  # проверка поля Hobbies
    browser.element('tr:nth-child(8) td:nth-child(2)').should(have.text(FILE))  # проверка поля Picture
    browser.element('tr:nth-child(9) td:nth-child(2)').should(have.text(ADDRESS))  # проверка поля Address
    browser.element('tr:nth-child(10) td:nth-child(2)').should(
        have.text(f'{STATE} {CITY}'))  # проверка поля State and City
    browser.element(by.id('closeLargeModal')).click()  # нажатие кнопки close
