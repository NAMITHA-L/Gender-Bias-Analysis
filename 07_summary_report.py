import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

# --- Define stereotype tags
stereotype_tags = {
    "Appearance": ["beautiful", "young", "pretty", "cute", "sexy", "hot", "attractive", "gorgeous", "slim", "fair"],
    "Agency": ["brave", "independent", "strong", "smart", "bold", "determined", "rebellious"],
    "Emotion": ["emotional", "caring", "kind", "sensitive", "loving", "loyal"],
    "Relationship": ["wife", "mother", "daughter", "girlfriend", "sister", "lover"],
}

# --- Clean & flatten function
def clean_and_flatten(df, column):
    all_words = []
    for entry in df[column].dropna():
        if entry.strip() == "[]":
            continue
        words = re.findall(r'\b\w+\b', entry)
        cleaned = [w.lower().strip() for w in words if w.strip()]
        all_words.extend(cleaned)
    return all_words

# --- Classify adjectives into stereotype tags
def classify_words(words, tag_dict):
    tag_counts = {k: 0 for k in tag_dict}
    for word in words:
        for tag, keywords in tag_dict.items():
            if word in keywords:
                tag_counts[tag] += 1
    return tag_counts

# --- Load adjective CSVs
female_df = pd.read_csv("data/female_adjectives.csv")
male_df = pd.read_csv("data/male_adjectives.csv")

# --- Clean and flatten
female_words = clean_and_flatten(female_df, "adjectives")
male_words = clean_and_flatten(male_df, "adjectives")

# --- Count most common
top_female = Counter(female_words).most_common(10)
top_male = Counter(male_words).most_common(10)

# --- Tag distribution
female_tags = classify_words(female_words, stereotype_tags)
male_tags = classify_words(male_words, stereotype_tags)

# --- Bias ratio
appearance_bias_ratio = 100 * female_tags["Appearance"] / max(1, len(female_words))

# --- Save report to text
with open("gender_bias_report.txt", "w", encoding="utf-8") as f:
    f.write("\n SUMMARY REPORT\n")
    f.write("--------------------------------------------------\n")
    f.write("Top 10 Female Adjectives:\n")
    for word, count in top_female:
        f.write(f"  - {word}: {count}\n")

    f.write("\nTop 10 Male Adjectives:\n")
    for word, count in top_male:
        f.write(f"  - {word}: {count}\n")

    f.write("\n Stereotype Tag Distribution (Female):\n")
    for k, v in female_tags.items():
        f.write(f"  - {k}: {v}\n")

    f.write("\n Stereotype Tag Distribution (Male):\n")
    for k, v in male_tags.items():
        f.write(f"  - {k}: {v}\n")

    f.write(f"\n Appearance-related bias in female descriptors: {appearance_bias_ratio:.1f}%\n")
    f.write("\nSee: gender_adjectives_bargraph.png\n")

print("✅ Text report saved as gender_bias_report.txt")

# --- Bar graph: comparison of top adjectives
top_female_dict = dict(top_female)
top_male_dict = dict(top_male)

all_keywords = sorted(set(top_female_dict) | set(top_male_dict))
x = np.arange(len(all_keywords))

female_counts = [top_female_dict.get(word, 0) for word in all_keywords]
male_counts = [top_male_dict.get(word, 0) for word in all_keywords]

# --- Plot
width = 0.35
plt.figure(figsize=(12, 6))
plt.bar(x - width/2, female_counts, width, label='Female', color='orange')
plt.bar(x + width/2, male_counts, width, label='Male', color='blue')

plt.xticks(x, all_keywords, rotation=45, ha='right')
plt.ylabel('Frequency')
plt.title('Top Adjectives by Gender')
plt.legend()
plt.tight_layout()

# --- Save chart
plt.savefig("gender_adjectives_bargraph.png", dpi=300)
plt.close()

print("✅ Bar graph saved as gender_adjectives_bargraph.png")
