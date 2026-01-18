🏆 Bestseller Product Tracker
📌 Overview

This project automatically tracks best-selling and trending products from public pages of multiple e-commerce websites (mainly Shopify) and updates the results daily in Google Sheets.

The system is built using 100% open-source technologies, requires no login access, and is intended for market research and competitive analysis.

🎯 What This Tool Does

Visits public/front pages of e-commerce websites

Identifies Best Seller / Trending products

Extracts public product data:

Product name

Price

Rating & review count

Bestseller / trending tags (if available)

Product URL

Calculates a Best-Seller Score

Automatically updates Google Sheets every day

🧠 How Best-Selling Products Are Identified

If a website does not explicitly mark a product as “Best Seller”, the system uses public signals:

Best-Seller Score =
(Review Count × 40%)
+ (Rating × 20%)
+ (Position on Page × 20%)
+ (Stock / Fast-Moving Signal × 20%)


This produces a realistic popularity ranking without accessing private sales data.

📊 Output (Google Sheets)

The bot creates and updates a Google Sheet with multiple tabs:

📄 Sheet 1: Raw Product Data

All collected products from all websites

🏆 Sheet 2: Daily Top Sellers

Ranked list of best-selling products

📈 Sheet 3: Trend Changes

New trending products

Rank increases and decreases

🧱 Technology Stack (Open Source)

Python

Playwright – for page loading and scrolling

BeautifulSoup – HTML parsing

Google Sheets API – reporting

Cron Job – daily automation

No paid tools or SaaS platforms are required.

📁 Project Structure
bestseller-tracker/
│
├── README.md
├── requirements.txt
│
├── config/
│   └── websites.yaml
│
├── scraper/
│   └── shopify_scraper.py
│
├── ranking/
│   └── bestseller_score.py
│
├── output/
│   └── google_sheets.py
│
├── scheduler/
│   └── run_daily.sh
│
└── main.py

⚙️ Configuration
1️⃣ Add Websites to Track

Edit the file:

config/websites.yaml


Example:

websites:
  - name: Website One
    url: https://example1.com
    platform: shopify

  - name: Website Two
    url: https://example2.com
    platform: shopify


You only need to paste website URLs — no coding required.

⏱ Automation

The system runs once every 24 hours

Fully automatic after setup

Frequency can be changed if needed

🔐 Legal & Ethical Use

Only public pages are accessed

No login, checkout, or private data

Rate-limited scraping

Intended strictly for research and analysis

🎯 Who This Is For

D2C brand owners

E-commerce teams

Market research analysts

Product and pricing strategy teams

📌 Notes

Optimized for Shopify websites

Mixed platforms supported

Easily scalable to more websites

🧑‍💻 Maintenance

This repository is structured so any Python developer can run and maintain it.

The repository owner does not need technical knowledge.

🚀 Future Enhancements

AI-based trend summaries

Email / WhatsApp alerts

Category-wise analysis

Price change tracking
