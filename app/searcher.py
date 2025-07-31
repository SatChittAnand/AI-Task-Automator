from playwright.sync_api import sync_playwright

def search_topic(topic):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.google.com/search?q={topic}")
        
        results = page.query_selector_all("div.BNeawe.s3v9rd.AP7Wnd")
        text_blocks = [r.inner_text() for r in results[:5]]
        
        browser.close()
        return " ".join(text_blocks)
