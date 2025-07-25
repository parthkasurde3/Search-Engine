#CS 600 (Advanced Algorithm Design and Implementation) - Search Engine Project
#By - Parth Kasurde (pkasurde@stevens.edu)
#CWID: 20022424

import nltk
from nltk.corpus import stopwords

import os
import re
from bs4 import BeautifulSoup
from collections import defaultdict

# Download stopwords from NLTK if not already present
nltk.download('stopwords')  # Ensure stopwords are available

class IndexNode:
    def _init_(self):
        self.children = {}  # Child characters in the trie
        self.is_complete_word = False  # Marks if node ends a word
        self.occurrence_map = defaultdict(int)  # File: frequency map

# The indexing trie
class WordIndex:
    def _init_(self):
        self.head = IndexNode()  # Starting point of trie

    def insert(self, token, doc):
        token = token.lower()
        current = self.head
        for ch in token:
            if ch not in current.children:
                current.children[ch] = IndexNode()
            current = current.children[ch]
        current.is_complete_word = True
        current.occurrence_map[doc] += 1

    def search(self, token):
        current = self.head
        for ch in token:
            if ch not in current.children:
                return None
            current = current.children[ch]
        return current.occurrence_map if current.is_complete_word else None


class SimpleSearchEngine:
    def _init_(self, source_folder):
        self.source_folder = source_folder
        self.index = WordIndex()

        nltk_common = set(stopwords.words("english"))

        additional_excludes = set([
            "also", "could", "might", "shall", "should", "would", "must", "may", "can", 
            "we", "us", "our", "you", "your", "he", "she", "it", "they", "their", 
            "my", "mine", "hers", "his", "theirs", "its", "because", "over", "under", 
            "above", "below", "again", "here", "there", "why", "how", "withal", "whereby"
        ])

        self.ignore_words = nltk_common.union(additional_excludes)

    def extract_text(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            html = BeautifulSoup(file, 'html.parser')
            return html.get_text()

    def tokenize_clean(self, raw_text):
        tokens = re.findall(r'\b\w+\b', raw_text.lower())
        return [word for word in tokens if word not in self.ignore_words]

    def create_index(self):
        for doc in os.listdir(self.source_folder):
            full_path = os.path.join(self.source_folder, doc)
            if doc.endswith('.html') and os.path.isfile(full_path):
                content = self.extract_text(full_path)
                words = self.tokenize_clean(content)
                for w in words:
                    self.index.insert(w, doc)

    def query(self, search_input):
        terms = search_input.lower().split()
        query_results = []
        for term in terms:
            hits = self.index.search(term)
            if hits:
                ranked = sorted(hits.items(), key=lambda x: x[1], reverse=True)
                query_results.append((term, ranked))
            else:
                query_results.append((term, "No results found"))
        return query_results


if _name_ == "_main_":
    data_path = r"C:\Users\ramna\Downloads\Search_Engine-main\Search_Engine-main\data"
    result_log = "output.txt"

    engine = SimpleSearchEngine(data_path)
    engine.create_index()

    print("Welcome to Parth's Search Engine!")
    print("Type your keywords below (type 'exit' to quit):\n")

    with open(result_log, 'w', encoding='utf-8') as out_file:
        out_file.write("Search Engine Output Log - By Parth\n\n")

    while True:
        input_query = input("Search for -> ").strip()
        if input_query.lower() == "exit":
            break

        with open(result_log, 'a', encoding='utf-8') as out_file:
            out_file.write(f"Query: {input_query}\n")

        if not input_query:
            print("None (Empty query)")
            with open(result_log, 'a', encoding='utf-8') as out_file:
                out_file.write("None (Empty query)\n\n")
            continue

        distinct_terms = set(word.lower() for word in input_query.split())

        for term in distinct_terms:
            result_set = engine.query(term)

            if all(res[1] == "No results found" for res in result_set):
                print(f"No matches for '{term}'")
                with open(result_log, 'a', encoding='utf-8') as out_file:
                    out_file.write(f"No matches for '{term}'\n\n")
            else:
                total_hits = sum(freq for _, freq in result_set[0][1])
                print(f"Matches for '{term}' (Total Hits: {total_hits}):")
                with open(result_log, 'a', encoding='utf-8') as out_file:
                    out_file.write(f"Matches for '{term}' (Total Hits: {total_hits}):\n")
                for doc, freq in result_set[0][1]:
                    print(f"  {doc}: {freq} time(s)")
                    with open(result_log, 'a', encoding='utf-8') as out_file:
                        out_file.write(f"  {doc}: {freq} time(s)\n")
                with open(result_log, 'a', encoding='utf-8') as out_file:
                    out_file.write("\n")