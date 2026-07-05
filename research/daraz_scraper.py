from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.price_parser import PriceParser

import time
import re


class DarazResearch:

    def __init__(self):

        options = Options()

        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)

    def _extract_sold(self, text):

        if not text:
            return 0

        text = text.lower().replace(",", "")

        m = re.search(r"(\d+)\s*sold", text)

        if m:
            return int(m.group(1))

        m = re.search(r"(\d+)\+", text)

        if m:
            return int(m.group(1))

        return 0

    def search(self, keyword):

        url = f"https://www.daraz.com.bd/catalog/?q={keyword}"

        self.driver.get(url)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.TAG_NAME, "body")
            )
        )

        time.sleep(5)

        products = self.driver.find_elements(

            By.CSS_SELECTOR,

            "div[data-qa-locator='product-item']"

        )

        results = []

        for item in products:

            try:

                name = item.find_element(

                    By.CSS_SELECTOR,

                    "div.RfADt a"

                ).text.strip()

                price = item.find_element(

                    By.CSS_SELECTOR,

                    "span.ooOxS"

                ).text.strip()

                sold_count = 0

                shop_name = ""

                try:

                    sold_text = item.find_element(

                        By.CSS_SELECTOR,

                        "div._6uN7R"

                    ).text.strip()

                    sold_count = self._extract_sold(
                        sold_text
                    )

                except:

                    pass

                #
                # Commit 064 এ এখানে Product Page visit করে
                # Seller Name collect করব
                #

                results.append({

                    "product": name,

                    "price": PriceParser.clean(price),

                    "sold_count": sold_count,

                    "shop_name": shop_name,

                    "market": "Daraz"

                })

            except:

                continue

        return results

    def close(self):

        self.driver.quit()