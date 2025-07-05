from collections import Counter
import pandas as pd
import re

# Define stereotype categories
bias_categories = {
    "appearance": ["beautiful", "sexy", "pretty", "young", "hot", "attractive", "lovely"],
    "agency": ["strong", "brave", "decides", "leads", "runs", "fights", "wins", "saves"],
    "relationship": ["wife", "mother", "daughter", "sister", "girlfriend"],
    "emotion": ["emotional", "caring", "crying", "angry", "upset", "nervous", "happy", "loving"]
}

def extract_words(cell):
    if not isinstance(cell, str):
        return []
    return [match for match in re.findall(r"'(.*?)'|\"(.*?)\"|([a-zA-Z]+)", cell)]

def clean_and_flatten(df, column):
    words = []
    for cell in df[column]:
        for match in extract_words(cell):
            word = next(filter(None, match)).lower()
            words.append(word)
    return words

def tag_bias(words):
    category_counts = Counter()
    for word in words:
        found = False
        for category, keywords in bias_categories.items():
            if word in keywords:
                category_counts[category] += 1
                found = True
                break
        if not found:
            category_counts["other"] += 1
    return category_counts

# Load female adjective and verb data
adj_df = pd.read_csv("data/female_adjectives.csv")
verb_df = pd.read_csv("data/female_verb.csv")

# Extract and clean
adjectives = clean_and_flatten(adj_df, "adjectives")
verbs = clean_and_flatten(verb_df, "verbs")

# Tag stereotype categories
adj_bias = tag_bias(adjectives)
verb_bias = tag_bias(verbs)

# Print results
print("\n🧠 Adjective Bias Categories:")
for cat, count in adj_bias.items():
    print(f"{cat.capitalize()}: {count}")

print("\n🧠 Verb Bias Categories:")
for cat, count in verb_bias.items():
    print(f"{cat.capitalize()}: {count}")
