# ranking/bestseller_score.py
# -----------------------------------
# Best-seller scoring logic
# -----------------------------------

def calculate_bestseller_score(products):
    """
    Assigns a simple best-seller score to each product
    based on public signals.
    """

    scored_products = []

    position = 1
    for product in products:
        score = 0

        # Position signal (top products assumed more popular)
        score += max(0, 100 - position * 2)

        scored_products.append({
            "website": product.get("website"),
            "product_name": product.get("product_name"),
            "product_url": product.get("product_url"),
            "score": score
        })

        position += 1

    return scored_products
