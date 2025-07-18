from pydantic import BaseModel, HttpUrl

class ShopifyURLRequest(BaseModel):
    url: HttpUrl

class ShopifyInsights(BaseModel):
    title: str
    description: str
    favicon: str | None = None
