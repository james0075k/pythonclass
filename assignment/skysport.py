import requests
from bs4 import BeautifulSoup
import os

BASE_URL = "https://www.skysports.com"
HEADERS = {"User-Agent": "Mozilla/5.0"}

os.makedirs("assignment", exist_ok=True)

def soup(url):
    return BeautifulSoup(requests.get(url, headers=HEADERS).text, "html.parser")

# Step 1: Load football news page
home = soup(BASE_URL + "/football/news")

# Step 2: Collect article links
links = set()
for a in home.find_all("a", href=True):
    if "/football/news/" in a["href"]:
        links.add(BASE_URL + a["href"])

print(f"Found {len(links)} football articles")

# Step 3: Scrape articles and save to TXT
with open("assignment/sky_sports_football.txt", "w", encoding="utf-8") as f:
    for url in list(links)[:10]:  # limit to 10
        page = soup(url)

        title = page.find("h1")
        paragraphs = page.find_all("p")

        if not title or not paragraphs:
            continue

        f.write(f"TITLE: {title.get_text(strip=True)}\n")
        f.write(f"URL: {url}\n\n")

        for p in paragraphs:
            f.write(p.get_text(strip=True) + "\n")

        f.write("\n" + "=" * 80 + "\n\n")

print("Saved football news to assignment/sky_sports_football.txt")