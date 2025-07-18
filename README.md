# Shopify Store Insights-Fetcher API

A Python-based FastAPI project to extract structured brand insights from Shopify-based web stores without using the official Shopify API.

---

## 🧩 Problem Statement

**Shopify** is one of the most popular platforms for D2C businesses to build online stores. Our goal is to extract important brand information from public Shopify store URLs and structure it in a usable JSON format. The extracted data includes product catalog, brand story, policies, contact details, social handles, and more.

This API fetches and organizes a Shopify store's web content into a structured JSON object. The implementation ensures clean design, scalability, and maintainability by following industry best practices like OOP, SOLID principles, and RESTful conventions.

---

## 🎯 Key Features

### ✅ Mandatory Requirements Implemented
- [x] Fetch Whole Product Catalog (`/products.json`)
- [x] Extract Hero Products (from homepage)
- [x] Extract Privacy Policy and Return/Refund Policies
- [x] Extract FAQs listed on site
- [x] Detect and parse brand’s social media handles
- [x] Extract brand contact information (emails, phone numbers)
- [x] Extract Brand Story or About the Brand
- [x] Extract key links like Order Tracking, Contact Us, Blogs
- [x] Expose `/get-insights?website_url=<shopify-store-url>` API route with structured JSON response

### 🚀 Bonus Features (Implemented)
- [x] Competitor Analysis using Google Search (basic)
- [x] Store structured insights and metadata in MySQL Database

---

## 📦 Tech Stack

- **Backend Framework:** FastAPI
- **Language:** Python 3.10+
- **Database:** MySQL (via SQLAlchemy ORM)
- **Web Scraping:** BeautifulSoup, Requests
- **LLM Integration:** (Optional, for structuring messy data)
- **Testing:** Postman Collection / Swagger UI
- **Deployment Ready:** Localhost with `uvicorn`, extensible to Docker or cloud

---

## 🛠 Project Structure

```plaintext
shopify-insights-fetcher/
├── app.py                   # Main Flask application
├── scraper.py              # Web scraping logic
├── utils.py                # Utility functions (e.g. URL cleaners, validators)
├── models.py               # Data models and schemas
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── .gitignore              # Ignored files
```


---

## 🔍 How It Works

### 1. **API Endpoint**
`GET /get-insights?website_url=https://example-shop.myshopify.com`

Returns JSON response:
```json
{
  "store_name": "Example Brand",
  "hero_products": [...],
  "product_catalog": [...],
  "privacy_policy": "...",
  "return_policy": "...",
  "faqs": [...],
  "about_us": "...",
  "social_links": {
    "instagram": "...",
    "facebook": "...",
    "youtube": "..."
  },
  "contact": {
    "emails": [...],
    "phone_numbers": [...]
  },
  "important_links": {
    "order_tracking": "...",
    "contact_us": "...",
    "blogs": "..."
  }
}


