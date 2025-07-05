import pandas as pd
import ast
import re
from collections import Counter

# --------- CLEANING HELPERS --------- #

def clean_text_list(raw_entry):
    if pd.isna(raw_entry):
        return []

    raw_entry = str(raw_entry).strip()
    raw_entry = re.sub(r"\[{2,}", "[", raw_entry)
    raw_entry = re.sub(r"\]{2,}", "]", raw_entry)

    try:
        parsed = ast.literal_eval(raw_entry)
        if isinstance(parsed, list):
            return [str(item).strip() for item in parsed if item]
    except (ValueError, SyntaxError):
        pass

    return re.findall(r"\b[a-zA-Z]+\b", raw_entry)

# --------- LOAD RAW FILES --------- #

female_verb = pd.read_csv("data/female_verb.csv")
female_adj = pd.read_csv("data/female_adjectives.csv")
male_verb = pd.read_csv("data/male_verb.csv")
male_adj = pd.read_csv("data/male_adjectives.csv")

# --------- CLEAN FEMALE VERBS --------- #

female_verb_columns = female_verb.columns[1:]  # All columns except 'year'

def merge_verb_columns(row):
    items = []
    for col in female_verb_columns:
        cell = row[col]
        if pd.notna(cell):
            items.extend(re.findall(r"[a-zA-Z]+", str(cell)))
    return items

female_verb["verbs"] = female_verb.apply(merge_verb_columns, axis=1)
female_verb = female_verb[["year", "verbs"]]
female_verb["verbs"] = female_verb["verbs"].apply(lambda x: [v.strip() for v in x if v])

# --------- CLEAN OTHERS --------- #

female_adj["adjectives"] = female_adj["adjectives"].apply(clean_text_list)
male_verb["verbs"] = male_verb["verbs"].apply(clean_text_list)
male_adj["adjectives"] = male_adj["adjectives"].apply(clean_text_list)

# --------- WORD FREQUENCIES --------- #

female_verb_freq = Counter([v for sublist in female_verb["verbs"] for v in sublist])
male_verb_freq = Counter([v for sublist in male_verb["verbs"] for v in sublist])
female_adj_freq = Counter([a for sublist in female_adj["adjectives"] for a in sublist])
male_adj_freq = Counter([a for sublist in male_adj["adjectives"] for a in sublist])

# --------- PRINT TOP WORDS --------- #

print("\n🔝 Top 10 Female Verbs:", female_verb_freq.most_common(10))
print("🔝 Top 10 Male Verbs:", male_verb_freq.most_common(10))
print("🔝 Top 10 Female Adjectives:", female_adj_freq.most_common(10))
print("🔝 Top 10 Male Adjectives:", male_adj_freq.most_common(10))
