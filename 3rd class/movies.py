import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os

BASE_URL = "https://new2.hdhub4u.fo/"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Educational Web Scraper)"
}

# Request homepage
response = requests.get(BASE_URL, headers=HEADERS, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

# Find all post cards (movies/series)
posts = soup.find_all("div", class_="post")

scraped_data = []

for post in posts:
    title_tag = post.find("h2")
    link_tag = post.find("a")

    if title_tag and link_tag:
        title = title_tag.get_text(strip=True)
        link = link_tag.get("href")

        scraped_data.append({
            "title": title,
            "url": link
        })

# Save to text file
base_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(base_dir, "hdhub4u_movies.txt")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("HDHub4u – Scraped Titles\n")
    f.write("Scraped at: " + datetime.now().isoformat() + "\n")
    f.write("=" * 50 + "\n\n")

    for item in scraped_data:
        f.write(f"Title: {item['title']}\n")
        f.write(f"URL  : {item['url']}\n")
        f.write("-" * 40 + "\n")

print("Scraping completed. Data saved to hdhub4u_movies.txt")