import requests
from bs4 import BeautifulSoup
from datetime import datetime
import os
import json

BASE_URL = "https://www.newtimes.co.rw"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Python Scraper)"
}

# --- Function to scrape a section page and return article URLs ---
def get_article_links(section_url):
    response = requests.get(section_url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    article_urls = []
    # Loop most articles (likely <a> tags in <h2>, <h3>, list items etc.)
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Only include internal article links
        if href.startswith("/"):
            full_link = BASE_URL + href
            if full_link not in article_urls:
                article_urls.append(full_link)
    return article_urls

# --- Function to extract details from an article page ---
def scrape_article(article_url):
    result = {}
    response = requests.get(article_url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title_tag = soup.find("h1")
    result["title"] = title_tag.get_text(strip=True) if title_tag else "No title"

    # Category (if present)
    result["category"] = None
    cat_tag = soup.find("h4")
    if cat_tag:
        result["category"] = cat_tag.get_text(strip=True)

    # Published date (if present)
    date_tag = soup.find("time")
    result["published_at"] = date_tag.get_text(strip=True) if date_tag else None

    # Content paragraphs
    content_text = []
    # Common article container might be <div> or <section>
    content_section = soup.find("div", class_="field-item")
    if not content_section:
        content_section = soup.find("section")
    if content_section:
        for p in content_section.find_all("p"):
            content_text.append(p.get_text(strip=True))

    result["content"] = "\n".join(content_text)

    result["url"] = article_url
    result["scraped_at"] = datetime.now().isoformat()
    return result

# ------------------ MAIN SCRAPING ------------------

# 1) Top general news (e.g., home or /news)
top_news_page = BASE_URL + "/news"
top_links = get_article_links(top_news_page)

# 2) Football news
football_page = BASE_URL + "/football"
football_links = get_article_links(football_page)

all_articles_data = []

print("Found top news:", len(top_links))
print("Found football news:", len(football_links))

# Scrape top news articles (limit first 5)
for url in top_links[:5]:
    data = scrape_article(url)
    data["section"] = "top"
    all_articles_data.append(data)

# Scrape football news articles (limit first 5)
for url in football_links[:5]:
    data = scrape_article(url)
    data["section"] = "football"
    all_articles_data.append(data)

# 3) Save to JSON file
base_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(base_dir, "newtimes_news.json")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_articles_data, f, indent=4, ensure_ascii=False)

print("Data saved to:", output_file)