import pandas as pd
import ast
from collections import Counter

# --- Define categories
stereotype_tags = {
    "Appearance": ["beautiful", "young", "pretty", "cute", "sexy", "hot", "attractive", "gorgeous", "slim", "fair"],
    "Agency": ["brave", "independent", "strong", "smart", "bold", "determined", "rebellious"],
    "Emotion": ["emotional", "caring", "kind", "sensitive", "loving", "loyal"],
    "Relationship": ["wife", "mother", "daughter", "girlfriend", "sister", "lover"],
}

# --- Cleaning function to convert string lists → real lists
import ast

import re

def clean_and_flatten(df, column):
    all_words = []
    for entry in df[column].dropna():
        # Skip completely empty entries
        if entry.strip() == "[]":
            continue

        # Extract words using regex from malformed list: [young] → 'young'
        words = re.findall(r'\b\w+\b', entry)
        cleaned = [w.lower().strip() for w in words if w.strip()]
        all_words.extend(cleaned)
    return all_words

# --- Tag classifier
def classify_words(words, tag_dict):
    tag_counts = {k: 0 for k in tag_dict}
    for word in words:
        for tag, keywords in tag_dict.items():
            if word in keywords:
                tag_counts[tag] += 1
    return tag_counts

# --- Load Data
female_df = pd.read_csv("data/female_adjectives.csv")
male_df = pd.read_csv("data/male_adjectives.csv")

# --- Clean & Flatten
female_words = clean_and_flatten(female_df, "adjectives")
male_words = clean_and_flatten(male_df, "adjectives")

# --- Count Top Words
top_female = Counter(female_words).most_common(10)
top_male = Counter(male_words).most_common(10)

# --- Tagging
female_tags = classify_words(female_words, stereotype_tags)
male_tags = classify_words(male_words, stereotype_tags)

# --- Bias Ratio
appearance_bias_ratio = 100 * female_tags["Appearance"] / max(1, len(female_words))

# --- 🖨️ Print Summary
print("\n SUMMARY REPORT")
print("--------------------------------------------------")
print("Top 10 Female Adjectives:")
for word, count in top_female:
    print(f"  - {word}: {count}")

print("\nTop 10 Male Adjectives:")
for word, count in top_male:
    print(f"  - {word}: {count}")

print("\n Stereotype Tag Distribution (Female):")
for k, v in female_tags.items():
    print(f"  - {k}: {v}")

print("\n Stereotype Tag Distribution (Male):")
for k, v in male_tags.items():
    print(f"  - {k}: {v}")

print(f"\n Appearance-related bias in female descriptors: {appearance_bias_ratio:.1f}%")
import matplotlib.pyplot as plt
import numpy as np

# --- Create a set of unique top adjectives from both genders ---
top_female = dict(Counter(female_words).most_common(10))
top_male = dict(Counter(male_words).most_common(10))

all_keywords = sorted(set(top_female.keys()).union(set(top_male.keys())))
x = np.arange(len(all_keywords))

# --- Align counts ---
female_counts = [top_female.get(word, 0) for word in all_keywords]
male_counts = [top_male.get(word, 0) for word in all_keywords]

# --- Plot ---
width = 0.35
plt.figure(figsize=(12, 6))
plt.bar(x - width/2, female_counts, width, label='Female', color='orange')
plt.bar(x + width/2, male_counts, width, label='Male', color='blue')

plt.xticks(x, all_keywords, rotation=45, ha='right')
plt.ylabel('Frequency')
plt.title('Top Adjectives by Gender')
plt.legend()
plt.tight_layout()

# Save and show
plt.savefig("gender_adjectives_bargraph.png", dpi=300)
plt.show()
