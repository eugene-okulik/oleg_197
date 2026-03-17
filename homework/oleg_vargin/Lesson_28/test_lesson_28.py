from playwright.sync_api import Page, expect
import time


def test_form_authentication(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    page.get_by_role('textbox', name='Username').fill('tomsmith')
    page.get_by_role('textbox', name='Password').fill('SuperSecretPassword!')
    page.get_by_role('button', name='Login').click()
    logout_btn = page.get_by_role('link', name='Logout')
    expect(logout_btn).to_be_visible()


def test_fill_automation_practice_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('testOleg')
    page.get_by_placeholder('Last Name').fill('testTest')
    page.get_by_placeholder('name@example.com').fill('test@example.com')
    page.locator('#gender-radio-1').check()
    page.get_by_placeholder('Mobile Number').fill('1234567890')
    page.locator('#dateOfBirthInput').click()
    page.locator('.react-datepicker__day--001').first.click()

    subjects_input = page.locator('#subjectsInput')
    subjects_input.type('Computer Science')
    page.locator('.subjects-auto-complete__menu').get_by_text(
        'Computer Science').click()

    page.get_by_text('Sports').check()
    page.get_by_text('Reading').check()
    page.get_by_text('Music').check()

    page.get_by_placeholder('Current Address').fill('123 Lenina St., Vladimir')

    page.locator('#state').click()

    page.get_by_text('NCR').click()

    page.locator('#city').click()
    page.get_by_text('Noida').click()
    page.locator('#submit').click()

    expect(page.locator('#closeLargeModal')).to_be_visible()
