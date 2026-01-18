# output/google_sheets.py
# -----------------------------------
# Google Sheets upload logic
# -----------------------------------

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def upload_to_google_sheets(scored_products, sheet_name="Bestseller Tracker"):
    """
    Uploads bestseller data to Google Sheets
    """

    # Google Sheets access scope
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Credentials file (developer will add this later)
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "google_credentials.json",
        scope
    )

    client = gspread.authorize(creds)

    # Open or create sheet
    try:
        sheet = client.open(sheet_name)
    except Exception:
        sheet = client.create(sheet_name)

    worksheet = sheet.sheet1
    worksheet.clear()

    # Header row
    worksheet.append_row([
        "Website",
        "Product Name",
        "Product URL",
        "Best Seller Score"
    ])

    # Data rows
    for product in scored_products:
        worksheet.append_row([
            product.get("website"),
            product.get("product_name"),
            product.get("product_url"),
            product.get("score")
        ])

