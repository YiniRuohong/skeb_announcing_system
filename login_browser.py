import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LOGIN_URL = "https://skeb.jp/login"


def main():
    opts = Options()
    opts.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=opts)
    driver.get(LOGIN_URL)
    print("Please log in via Twitter/X in the browser window.")
    input("Press Enter after completing the login...")
    cookies = driver.get_cookies()
    driver.quit()
    cookie_str = "; ".join(f"{c['name']}={c['value']}" for c in cookies if c.get('domain') == 'skeb.jp')
    with open("skeb_storage.json", "w", encoding="utf-8") as f:
        json.dump({"cookie": cookie_str}, f, ensure_ascii=False, indent=2)
    print("Cookies saved to skeb_storage.json")


if __name__ == "__main__":
    main()
