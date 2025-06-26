# modules/academic_scraper.py
import requests
from bs4 import BeautifulSoup

SEARCH_URLS = {
    "IEEE": "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText={}",
    "Springer": "https://link.springer.com/search?query={}",
    "ACM": "https://dl.acm.org/action/doSearch?AllField={}"
}

GAP_KEYWORDS = [
    "open problem", "open question", "future work", "further research",
    "remains unexplored", "not yet addressed", "unresolved issue",
    "research challenge", "open challenge", "limitation of this study",
    "still unclear", "requires investigation", "scope for improvement",
    "future direction", "requires further study", "not fully understood"
]

def fetch_academic_gaps(query):
    results = []
    headers = {"User-Agent": "Mozilla/5.0"}
    for source, url_template in SEARCH_URLS.items():
        url = url_template.format(query.replace(" ", "+"))
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(resp.text, "html.parser")
            papers = soup.find_all(["article", "li", "div"], limit=10)
            for paper in papers:
                text = paper.get_text(separator=" ", strip=True).lower()
                if not any(kw in text for kw in GAP_KEYWORDS):
                    continue
                if "2025" not in text:
                    continue
                title_tag = paper.find("h2") or paper.find("h3") or paper.find("a")
                title = title_tag.get_text(strip=True) if title_tag else "No title found"
                href = title_tag.get("href", "") if title_tag else ""
                link = href if href.startswith("http") else f"{url}{href}"
                results.append({
                    "source": source,
                    "title": title,
                    "summary": f"Detected gap keyword and '2025' in text.",
                    "gap_found": "keyword + 2025",
                    "link": link,
                    "published": "2025",
                    "topic": query
                })
        except Exception as e:
            print(f"[!] Error scraping {source}: {e}")
            continue
    return results
