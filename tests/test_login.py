from playwright.sync_api import Page, expect

URL = "https://the-internet.herokuapp.com/login"

def test_login_sucesso(page: Page):
    page.goto(URL)
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type=submit]")
    expect(page.locator(".flash.success")).to_contain_text("You logged into a secure area!")

def test_login_falha(page: Page):
    page.goto(URL)
    page.fill("#username", "userinvalido")
    page.fill("#password", "senhainvalida")
    page.click("button[type=submit]")
    expect(page.locator(".flash.error")).to_contain_text("Your username is invalid!")
