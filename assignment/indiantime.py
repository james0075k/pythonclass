import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os

BASE_URL = "https://timesofindia.indiatimes.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

os.makedirs("assignment", exist_ok=True)

def fetch_page(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        return BeautifulSoup(r.text, "html.parser")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# Fetch homepage
home_soup = fetch_page(BASE_URL)
if not home_soup:
    exit("Could not load TOI homepage")

# ✅ Collect article links safely
trending_links = set()

for a in home_soup.find_all("a", href=True):
    href = a["href"]

    if ".cms" in href and not href.startswith("javascript"):
        if href.startswith("/"):
            trending_links.add(BASE_URL + href)
        elif href.startswith("http"):
            trending_links.add(href)

trending_links = list(trending_links)
print(f"Found {len(trending_links)} article URLs")

articles_data = []

for url in trending_links[:15]:  # limit for safety
    soup = fetch_page(url)
    if not soup:
        continue

    # Title
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else None

    # Publish date
    publish_date = None
    byline = soup.find("div", class_="byline")
    if byline:
        publish_date = byline.get_text(strip=True)

    # Content
    content = ""
    body = soup.find("div", itemprop="articleBody")
    if body:
        paragraphs = body.find_all("p")
        content = "\n".join(p.get_text(strip=True) for p in paragraphs)

    articles_data.append({
        "title": title,
        "publish_date": publish_date,
        "content": content,
        "url": url,
        "scraped_at": datetime.now().isoformat()
    })

# ✅ Save JSON (FIXED PATH)
with open("assignment/times_of_india_trending.json", "w", encoding="utf-8") as f:
    json.dump(articles_data, f, ensure_ascii=False, indent=4)

print("Saved scraped data to assignment/times_of_india_trending.json")