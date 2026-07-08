from playwright.sync_api import sync_playwright


def log_response(response):

    url = response.url.lower()

    if any(x in url for x in [
        "search",
        "catalog",
        "mtop",
        "api",
        "graphql"
    ]):

        print("=" * 100)
        print(response.status)
        print(response.url)
        print("=" * 100)


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.on("response", log_response)

    page.goto("https://www.daraz.com.bd/catalog/?q=usb+blender")

    input("Press ENTER after page fully loads...")

    browser.close()