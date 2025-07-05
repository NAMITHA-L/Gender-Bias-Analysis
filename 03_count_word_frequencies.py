import pandas as pd
import re
from collections import Counter

def extract_words(cell):
    if not isinstance(cell, str):
        return []
    # Extract words between quotes or bare words inside square brackets
    return re.findall(r"'(.*?)'|\"(.*?)\"|([a-zA-Z]+)", cell)

def clean_and_flatten(df, column):
    words = []
    for cell in df[column]:
        for match in extract_words(cell):
            # match is a tuple due to multiple capture groups — get the first non-empty one
            word = next(filter(None, match))
            words.append(word.lower())
    return words

# Load data
female_adj_df = pd.read_csv("data/female_adjectives.csv")
female_verb_df = pd.read_csv("data/female_verb.csv")

# Clean and extract
adjectives = clean_and_flatten(female_adj_df, "adjectives")
verbs = clean_and_flatten(female_verb_df, "verbs")

# Count
adj_counter = Counter(adjectives)
verb_counter = Counter(verbs)

# Print
print("\n🔤 Top 10 Adjectives for Female Characters:")
for word, count in adj_counter.most_common(10):
    print(f"{word}: {count}")

print("\n🔤 Top 10 Verbs for Female Characters:")
for word, count in verb_counter.most_common(10):
    print(f"{word}: {count}")
