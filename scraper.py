import requests
from bs4 import BeautifulSoup
from models import ShopifyInsights

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_shopify_insights(url: str) -> ShopifyInsights:
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise ValueError(f"Error fetching the URL: {e}")

    soup = BeautifulSoup(response.text, 'html.parser')

    title_tag = soup.find("title")
    meta_desc = soup.find("meta", attrs={"name": "description"})
    favicon_tag = soup.find("link", rel="icon") or soup.find("link", rel="shortcut icon")

    return ShopifyInsights(
        title=title_tag.text.strip() if title_tag else "No title found",
        description=meta_desc['content'].strip() if meta_desc and meta_desc.has_attr('content') else "No description found",
        favicon=favicon_tag['href'] if favicon_tag and favicon_tag.has_attr('href') else None
    )
