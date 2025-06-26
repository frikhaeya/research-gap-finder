# modules/scholar_scraper.py
from serpapi import GoogleSearch
from modules.arxiv_scraper import GAP_KEYWORDS
import os

SERP_API_KEY = os.getenv("SERP_API_KEY")  # Store your API key in .env or environment

def fetch_scholar_gaps(query):
    results = []
    search = GoogleSearch({
        "q": f"{query} open problems",
        "hl": "en",
        "api_key": SERP_API_KEY,
        "engine": "google_scholar",
        "num": "20"
    })
    response = search.get_dict()

    for item in response.get("organic_results", []):
        snippet = item.get("snippet", "").lower()
        title = item.get("title")
        link = item.get("link")

        if any(k in snippet for k in GAP_KEYWORDS) and "2025" in snippet:
            results.append({
                "source": "Google Scholar (via SerpAPI)",
                "title": title,
                "summary": snippet,
                "gap_found": "keyword + 2025",
                "link": link,
                "published": "2025",
                "topic": query
            })

    return results

