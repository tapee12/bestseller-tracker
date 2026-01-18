# scraper/shopify_scraper.py
# -----------------------------------
# DO NOT TOUCH unless you are a developer
# Shopify public product scraper
# -----------------------------------

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time


def scrape_shopify_site(site_name, base_url):
    """
    Scrapes best-selling / trending products
    from a public Shopify website
    """

    products = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # Step 1: Open homepage
            page.goto(base_url, timeout=60000)
            time.sleep(5)

            # Step 2: Try common bestseller URLs
            possible_paths = [
                "/collections/best-sellers",
                "/collections/bestsellers",
                "/collections/trending",
                "/collections/popular",
                "/collections/all"
            ]

            target_url = None
            for path in possible_paths:
                test_url = base_url.rstrip("/") + path
                page.goto(test_url, timeout=60000)
                time.sleep(3)
                if "product" in page.content().lower():
                    target_url = test_url
                    break

            # Fallback to homepage if no collection found
            if not target_url:
                target_url = base_url

            page.goto(target_url, timeout=60000)
            time.sleep(5)

            # Step 3: Scroll to load products
            for _ in range(5):
                page.mouse.wheel(0, 3000)
                time.sleep(2)

            # Step 4: Parse HTML
            soup = BeautifulSoup(page.content(), "lxml")

            product_cards = soup.select("a[href*='/products/']")

            for card in product_cards:
                try:
                    product_url = card.get("href")
                    if not product_url.startswith("http"):
                        product_url = base_url.rstrip("/") + product_url

                    title = card.get_text(strip=True)
                    if not title:
                        continue

                    products.append({
                        "website": site_name,
                        "product_name": title[:120],
                        "product_url": product_url
                    })

                except Exception:
                    continue

        except Exception as e:
            print(f"[ERROR] {site_name}: {e}")

        finally:
            browser.close()

    return products
