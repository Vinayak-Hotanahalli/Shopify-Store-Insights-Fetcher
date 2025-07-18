def is_shopify_store(html_text: str) -> bool:
    return "cdn.shopify.com" in html_text or "myshopify.com" in html_text
