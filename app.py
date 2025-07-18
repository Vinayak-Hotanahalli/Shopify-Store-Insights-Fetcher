import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from urllib.parse import urljoin

app = FastAPI()

class ShopifyURL(BaseModel):
    url: str

@app.post("/get-insights")
def get_insights(data: ShopifyURL):
    try:
        base_url = data.url.rstrip('/')
        products_api_url = f"{base_url}/products.json"

        response = requests.get(products_api_url, headers={'User-Agent': 'Mozilla/5.0'})
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Products not found")

        product_data = response.json().get("products", [])

        products = []
        for product in product_data:
            products.append({
                "title": product.get("title", ""),
                "description": product.get("body_html", ""),  # ✅ Added description
                "image": product["images"][0]["src"] if product.get("images") else "",
                "price": product["variants"][0]["price"] if product.get("variants") else "",
                "product_url": f"{base_url}/products/{product.get('handle', '')}"
            })

        site_response = requests.get(base_url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(site_response.text, 'html.parser')

        title = soup.title.string.strip() if soup.title else ""
        favicon_tag = soup.find("link", rel="icon")
        favicon_url = favicon_tag['href'] if favicon_tag else ""

        if favicon_url and not favicon_url.startswith("http"):
            favicon_url = urljoin(base_url, favicon_url)

        return {
            "title": title,
            "description": "",
            "favicon": favicon_url,
            "products": products
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
