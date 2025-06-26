# modules/github_scraper.py
import requests
from datetime import datetime

GITHUB_API = "https://api.github.com/search/repositories?q={}&sort=stars&order=desc"

def fetch_github_gaps(query):
    headers = {"Accept": "application/vnd.github.v3+json"}
    q = f"{query} in:description created:2025-01-01..2025-12-31 help+wanted"
    results = []
    try:
        resp = requests.get(GITHUB_API.format(q.replace(" ", "+")), headers=headers)
        items = resp.json().get("items", [])
        for item in items[:10]:
            created = item.get("created_at", "")
            created_year = datetime.strptime(created, "%Y-%m-%dT%H:%M:%SZ").year if created else None
            if created_year != 2025:
                continue
            results.append({
                "source": "GitHub",
                "title": item.get("name"),
                "summary": item.get("description"),
                "gap_found": "GitHub repo flagged 'help wanted' (2025)",
                "link": item.get("html_url"),
                "published": created,
                "topic": query
            })
        return results
    except Exception as e:
        print(f"[!] GitHub API error: {e}")
        return []
