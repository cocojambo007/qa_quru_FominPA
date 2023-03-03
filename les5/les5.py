import time

from selene import browser, be, have, by


def test_les5(browser_setup):
    browser.element(by.id('firstName')).should(be.blank).type('Павел')  # поле first name
    browser.element(by.id('lastName')).should(be.blank).type('Фомин')  # поле last name
    browser.element(by.id('userEmail')).should(be.blank).type('test@test.ru')  # поле email
    browser.element('div[class*="custom-control"] label[for="gender-radio-1"]').click()  # выбор gender
    browser.element(by.id('userNumber')).should(be.blank).type('88005553535')  # поле телефон
    browser.element(by.id('dateOfBirthInput')).click()  # выбор поля день рождения
    browser.element('select[class="react-datepicker__month-select"] option[value="6"]').click()  # выбор месяца
    browser.element('select[class="react-datepicker__year-select"] option[value="1993"]').click()  # выбор года
    browser.element('div[class="react-datepicker__day react-datepicker__day--005"]').click()  # выбор даты
    browser.element(by.id('subjectsInput')).should(be.blank).type('Maths').press_enter()  # поле subject
    browser.element('div[class="custom-control custom-checkbox custom-control-inline"] label[for="hobbies-checkbox-1"]') \
        .click()  # выбор хобби
    browser.element(by.id('uploadPicture')).send_keys('C:/Users/FominPA/PycharmProjects/qa_quru_FominPA/les5/resources/Screenshot_1.jpg')  # загрузка файла
    browser.element(by.id('currentAddress')).should(be.blank).type('Current Address').click()  # поле адреса
    browser.element(by.id('react-select-3-input')).type('Uttar Pradesh').press_enter()  # выбор state
    browser.element(by.id('react-select-4-input')).type('Agra').press_enter()  # выбор city
    browser.element(by.id('submit')).click()  # нажатие кнопки submit
    browser.element(by.id('example-modal-sizes-title-lg')).should(have.text('Thanks for submitting the form'))  # проверка всплывающего окна
