# main.py
# -----------------------------------
# Main runner file
# -----------------------------------

import yaml

from scraper.shopify_scraper import scrape_shopify_site
from ranking.bestseller_score import calculate_bestseller_score
from output.google_sheets import upload_to_google_sheets


def load_websites():
    """Load websites from config file"""
    with open("config/websites.yaml", "r") as file:
        data = yaml.safe_load(file)
    return data.get("websites", [])


def main():
    all_products = []

    websites = load_websites()

    print(f"[INFO] Total websites loaded: {len(websites)}")

    for site in websites:
        name = site.get("name")
        url = site.get("url")
        platform = site.get("platform", "unknown")

        print(f"[INFO] Scraping: {name} ({platform})")

        if platform == "shopify":
            products = scrape_shopify_site(name, url)
            all_products.extend(products)
        else:
            print(f"[SKIP] Platform not supported yet: {platform}")

    print(f"[INFO] Total products collected: {len(all_products)}")

    # Calculate bestseller score
    scored_products = calculate_bestseller_score(all_products)

    # Upload to Google Sheets
    upload_to_google_sheets(scored_products)

    print("[SUCCESS] Google Sheet updated successfully!")


if __name__ == "__main__":
    main()
