import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

BASE_URL = "https://www.bbc.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

os.makedirs("assignment", exist_ok=True)

def get_soup(url):
    return BeautifulSoup(requests.get(url, headers=HEADERS).text, "html.parser")

# Step 1: Get homepage
home = get_soup(BASE_URL + "/news")

# Step 2: Collect article links
links = set()
for a in home.find_all("a", href=True):
    if a["href"].startswith("/news") and "/live/" not in a["href"]:
        links.add(BASE_URL + a["href"])

print(f"Found {len(links)} articles")

# Step 3: Scrape articles
with open("assignment/bbc_news.txt", "w", encoding="utf-8") as f:
    for url in list(links)[:10]:  # limit to 10
        soup = get_soup(url)

        title = soup.find("h1")
        body = soup.find_all("p")

        if not title or not body:
            continue

        f.write(f"TITLE: {title.get_text(strip=True)}\n")
        f.write(f"URL: {url}\n\n")

        for p in body:
            f.write(p.get_text(strip=True) + "\n")

        f.write("\n" + "=" * 80 + "\n\n")

print("Saved news to assignment/bbc_news.txt")