import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])
    page = browser.new_page(no_viewport=True)

    print("Открываю сайт...")
    page.goto("https://wikipedia.org")

    print("Ввожу поисковый запрос...")
    page.locator("#searchInput").fill("Автоматизированное тестирование")

    print("Нажимаю кнопку поиска...")
    page.locator("#searchInput").press("Enter")

    time.sleep(3)

    page.screenshot(path="search_results.png")
    print("Screenshot taken and saved")

    browser.close()