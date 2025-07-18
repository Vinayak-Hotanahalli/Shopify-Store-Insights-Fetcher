# 🛒 Shopify Store Insights Fetcher Application

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-Agent-yellow?logo=langchain)](https://www.langchain.com/)
[![Status](https://img.shields.io/badge/Status-In%20Progress-orange)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

> 🔍 Extracts insights from Shopify stores using FastAPI + LangChain agent.


## 🚀 Overview

This project is a Python-based backend system that fetches and organizes insights from Shopify-based e-commerce stores **without using the official Shopify API**. It is developed as part of the GenAI Developer Intern Assignment and follows best practices of backend design, RESTful architecture, and clean code.

The application extracts structured brand information such as product catalogs, hero products, privacy policies, FAQs, social media links, and more from a given Shopify store URL.

---

## 📁 Project Structure

| File/Folder        | Description                          |
|--------------------|--------------------------------------|
| `__pycache__/`     | Compiled Python files (auto-created) |
| `app.py`           | FastAPI or main application entry    |
| `main.py`          | Main routing or logic file           |
| `models.py`        | Defines data models/schema           |
| `scraper.py`       | Contains web scraping logic          |
| `utils.py`         | Helper/utility functions             |
| `requirements.txt` | Project dependencies list            |

---

## 📌 Features

- Extracts detailed brand insights from any Shopify store URL, including:
  - Entire Product Catalog
  - Hero Products (Homepage Highlights)
  - Privacy Policy
  - Return and Refund Policies
  - FAQs (Supports various formats)
  - Social Media Handles (Instagram, Facebook, etc.)
  - Contact Information (Emails, Phone Numbers)
  - About the Brand Section
  - Other Important Links (Order Tracking, Blogs, etc.)

- RESTful API built with FastAPI or Flask
- JSON responses with appropriate HTTP status codes
- Optional: Structured data persisted in a MySQL database (Bonus)
- Optional: Competitor Analysis and Insights Extraction (Bonus)


---
## 🛠 Tech Stack

| Component        | Technology     |
|------------------|----------------|
| Backend Language | Python         |
| Framework        | FastAPI / Flask|
| Database         | MySQL (optional) |
| Web Scraping     | BeautifulSoup, Requests |
| Deployment Ready | Yes (Postman/UI Supported) |

---


## 🔗 API Endpoint

### `POST /get-insights`

**Request:**

```json
{
  "url": "https://www.allbirds.com"
}

```

**Success Response (200):**

```json
{
  "brand_name": "Example Store",
  "products": [...],
  "hero_products": [...],
  "privacy_policy": "...",
  "refund_policy": "...",
  "faqs": [
    {
      "question": "...",
      "answer": "..."
    }
  ],
  "social_handles": {
    "instagram": "...",
    "facebook": "..."
  },
  "contact_info": {
    "email": "...",
    "phone": "..."
  },
  "about_brand": "...",
  "important_links": {
    "order_tracking": "...",
    "blogs": "...",
    "contact_us": "..."
  }
}
```

**Error Responses:**

* `401 Unauthorized` – If the given website is invalid or not found
* `500 Internal Server Error` – For any unhandled exceptions or runtime issues

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Vinayak-Hotanahalli/Shopify-Store-Insights-Fetcher.git
cd shopify-insights-fetcher
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

Using FastAPI:

```bash
uvicorn app:app --reload
```

Using Flask:

```bash
python app.py
```

### 4. Test via Postman or Browser

Visit: `http://127.0.0.1:8000/docs` (if using FastAPI)
or test API endpoint with Postman by sending `POST` request to `/get-insights`.

---

## ✅ Mandatory Tasks Implemented

* [x] Fetch Shopify website data without API
* [x] Extract structured insights (Products, Policies, FAQs, etc.)
* [x] REST API with error handling
* [x] Return JSON response
* [x] Followed clean code, OOP, SOLID principles

---

## ⭐ Bonus Section (If Implemented)

* [ ]  Competitor Analysis and Insights
* [ ]  Data Persistence using MySQL
* [ ]  LLM-based data structuring for unstructured pages

---

## 📎 References

* Example Shopify Sites:

  * [https://memy.co.in](https://memy.co.in)
  * [https://hairoriginals.com](https://hairoriginals.com)
* List of Shopify Stores:

  * [https://webinopoly.com/blogs/news/top-100-most-successful-shopify-stores](https://webinopoly.com/blogs/news/top-100-most-successful-shopify-stores)
* Shopify Pattern Hint:

  * `https://<shopify-site>/products.json`

---

## 👨‍💻 Developer Notes

* FAQs scraping supports both flat and paginated structures.
* Data is cleaned and normalized into structured formats.
* Modular codebase for maintainability and reusability.
* Easy to extend for future enhancements.

---

## 📬 Contact

**👤 Vinayak Girish Hotanahalli**  
📧 [vinayakhotanahalli72@gmail.com](mailto:vinayakhotanahalli72@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/vinayak-hotanahalli-2775b929b)  
🐙 [GitHub](https://github.com/Vinayak-Hotanahalli)

