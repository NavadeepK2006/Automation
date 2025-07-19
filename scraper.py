from playwright.sync_api import sync_playwright
import os
def fetch_chapter(url,screenshot_path):
    os.makedirs(os.path.dirname(screenshot_path),exist_ok=True)
    with sync_playwright() as p:
        browser=p.chromium.launch()
        page=browser.new_page()
        page.goto(url)
        page.screenshot(path=screenshot_path,full_page=True)
        content=page.inner_text("div#mw-content-text")
        browser.close()
    return content