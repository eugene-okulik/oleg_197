from playwright.sync_api import Page, expect, BrowserContext


def test_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm ')
    page.once('dialog', lambda dialog: dialog.accept())
    page.get_by_role('link', name='Click').click()
    expect(page.locator('#result-text')).to_have_text('Ok')


def test_active_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    with context.expect_page() as new_page:
        page.get_by_role('link', name='Click').click()
    expect(new_page.value.locator('#result-text')).to_have_text(
        'I am a new page in a new tab'
    )


def test_wait_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    red_text_button = page.locator('.text-danger')
    red_text_button.click()
