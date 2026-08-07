import httpx
from scrapling import Selector

def scrape(url: str):
    if not url or not url.strip():
        return ""

    response = httpx.get(url, timeout=30)
    response.raise_for_status()

    doc = Selector(response.text)
    context = doc.get_all_text()

    return context