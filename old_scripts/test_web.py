def test_wikipedia_search(page):
    page.goto("https://www.wikipedia.org/")
    page.locator("#searchInput").fill("Автоматизированное тестирование")
    page.locator("#searchInput").press("Enter")

    heading_text = page.locator("h1").inner_text()
    assert heading_text == "Автоматизированное тестирование"