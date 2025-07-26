# 🔍 CS 600 – Simplified Search Engine  
**Project Title:** Search Engine  
**Course:** CS 600 – Advanced Algorithm Design and Implementation  
**Student Name:** Parth Kasurde  
**CWID:** 20022424  
**Email:** pkasurde@stevens.edu  
**Institution:** Stevens Institute of Technology  

---

## 📁 Submitted Files

| File Name              | Description |
|------------------------|-------------|
| `project.py`           | Python code implementing the search engine using a Trie structure. |
| `output.txt`           | Sample run outputs for various search queries, including boundary tests. |
| `FINALVIDEO600.mov`    | Short demo video showing the execution and edge case testing. |
| `requirements.txt`     | List of required Python libraries (BeautifulSoup, NLTK). |
| *input                 | Stored locally and referenced in `project.py` for indexing and search. |

---

## 📌 Project Overview

This project implements a **simplified search engine** based on the design outlined in **Section 23.6 (Subsection: Search Engine)** of the course textbook. It indexes all relevant words from HTML files, excluding stopwords such as articles, prepositions, and pronouns. A **Trie** is used for indexing, and a basic ranking algorithm displays search results based on word frequency per document.

---

## 🛠️ Tools & Technologies Used

- **Python 3**
- **BeautifulSoup4** – For parsing HTML files  
- **NLTK** – For stopword filtering  
- **Trie (Prefix Tree)** – Main data structure for indexing and searching words  

---

## ⚙️ Implementation Summary

### ✅ Indexing Approach
- Parses text from HTML files using `BeautifulSoup`.
- Removes stopwords using NLTK’s built-in English stopword set.
- Each word is inserted into a **Trie**:
- Case-insensitive storage.
- Tracks frequency of each word in each HTML file.

### ✅ Searching & Ranking
- Search queries are case-insensitive.
- For each term, the program:
- Searches the Trie.
- Lists all files containing the term.
- Ranks them based on **term frequency**.

---

## 🔍 Sample Output

Shown in `output.txt`, queries such as:
- `"FA Cup"`
- `"league"`
- `"ball"`
- `"win"`

...return documents and exact word counts per file. Stopwords like `"the"`, `"your"`, `"he"` correctly return **no results**, confirming stopword filtering is effective.

---

## 📊 Boundary Conditions Tested

✔️ Case insensitivity  
✔️ No matches for non-existent terms  
✔️ Stopword exclusion  
✔️ Mixed multi-word queries  
✔️ Edge case queries (e.g., empty string, punctuation-only, etc.)

All outputs are shown in **`output.txt`**.

---

## ▶️ How to Run

1. **Install Required Packages:**

```bash
pip install -r requirements.txt
```

2. **Download NLTK Stopwords Once:**

```python
import nltk
nltk.download('stopwords')
```

3. **Run the Script:**

```bash
python project.py
```

> Note: Make sure your HTML files are placed in the correct path as referenced inside `project.py`.
