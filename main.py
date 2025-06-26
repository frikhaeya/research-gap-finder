# main.py
from modules.arxiv_scraper import fetch_arxiv_gaps
from modules.scholar_scraper import fetch_scholar_gaps
from modules.academic_scraper import fetch_academic_gaps
from modules.github_scraper import fetch_github_gaps
from utils.keywords import ALL_TOPICS as topics

import pandas as pd

all_results = []

for topic in topics:
    all_results += fetch_arxiv_gaps(topic)
    all_results += fetch_scholar_gaps(topic)
    all_results += fetch_academic_gaps(topic)
    all_results += fetch_github_gaps(topic)

# Save or display
df = pd.DataFrame(all_results)
df.to_csv("research_gaps.csv", index=False)
print(df.head())
