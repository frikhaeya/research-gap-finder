# 🔍 Research Gap Finder

This is a modular Python tool that scans **academic and professional sources** to identify **unsolved problems**, research gaps, or open issues in modern technical domains.

Currently supported topics include:

- 🔐 Post-Quantum Cryptography (PQC)
- 🛡️ Cybersecurity
- 🤖 AI in Cybersecurity

It queries platforms like:
- arXiv.org
- IEEE Xplore
- Springer
- ACM Digital Library
- GitHub

> 💡 Originally built to track unexplored research opportunities in Post-Quantum Cryptography and its intersection with cybersecurity and AI.

---

## 🛠 Installation

```bash
git clone https://github.com/your-username/research-gap-finder.git
cd research-gap-finder
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
You’ll need Python 3.8+ and a Unix-like environment (Linux/macOS/WSL).
```

## 🚀 Usage
```bash
python3 main.py
```

The output will be saved in:
research_gaps.csv
You can open it with Excel, Notion, VS Code, or any data tool.

## ⚙️ Customizing the Search
To look up your own research areas, go to:

```bash
utils/keywords.py
```

And modify the following lists:

```python
YOUR_TOPIC_KEYWORDS = [
  "robotics security",
  "blockchain forensics",
  "AI in medicine",
  ...
]

ALL_TOPICS = YOUR_TOPIC_KEYWORDS
Then run the tool again — it will scan those new topics for 2025 publications and GitHub trends.
```

## 📁 Project Structure
File	Purpose
main.py	Orchestrates the scan for all sources
modules/	Each data source has a module here
utils/keywords.py	Keyword config: edit this to change the focus
research_gaps.csv	Final output file

## 📌 Notes
Google Scholar scraping was removed due to rate limits. Use arXiv, Semantic Scholar, or official APIs instead.

The academic scrapers fetch and parse search result pages (not full paper PDFs).

## 📈 TODO / Ideas
 - Add Semantic Scholar API support

 - Filter papers by citation count or author h-index

 - Web UI for keyword control

 - Notion or Airtable export integration

## 🙋‍♀️ Contributing
Feel free to fork, adapt, or submit PRs if you want to:

Add more scrapers

Improve NLP-based gap detection

Connect to paid APIs like Dimensions.ai or Lens.org

🧠 Author
Developed by Eya Frikha (2025) for research automation and strategic academic planning.
