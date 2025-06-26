# modules/arxiv_scraper.py
import arxiv
GAP_KEYWORDS = [
    "open problem", "open question", "future work", "further research",
    "remains unexplored", "not yet addressed", "unresolved issue",
    "research challenge", "open challenge", "limitation of this study",
    "still unclear", "requires investigation", "scope for improvement",
    "future direction", "requires further study", "not fully understood"
]

def extract_gap(abstract):
    for pattern in GAP_KEYWORDS:
        if pattern in abstract.lower():
            return pattern
    return None

def fetch_arxiv_gaps(query):
    results = []
    search = arxiv.Search(query=query, max_results=30, sort_by=arxiv.SortCriterion.SubmittedDate)
    for result in search.results():
        if result.published.year != 2025:
            continue
        gap = extract_gap(result.summary)
        if gap:
            results.append({
                "source": "arXiv",
                "title": result.title,
                "summary": result.summary,
                "gap_found": gap,
                "link": result.entry_id,
                "published": result.published,
                "topic": query
            })
    return results

