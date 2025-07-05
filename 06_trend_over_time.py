from collections import Counter, defaultdict
import pandas as pd
import re
import matplotlib.pyplot as plt

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

def get_decade(year):
    try:
        y = int(year)
        return (y // 10) * 10
    except:
        return None

# Load data
female_adj = pd.read_csv("data/female_adjectives.csv")
female_adj["decade"] = female_adj["year"].apply(get_decade)

# Count category occurrences per decade
decade_category_counts = defaultdict(lambda: Counter())

for _, row in female_adj.iterrows():
    decade = row["decade"]
    if pd.isna(decade):
        continue
    words = []
    for match in extract_words(row["adjectives"]):
        word = next(filter(None, match)).lower()
        words.append(word)
    for word in words:
        found = False
        for category, keywords in bias_categories.items():
            if word in keywords:
                decade_category_counts[decade][category] += 1
                found = True
                break
        if not found:
            decade_category_counts[decade]["other"] += 1

# Prepare data for plotting
category_trends = defaultdict(list)
decades_sorted = sorted(decade_category_counts.keys())

for decade in decades_sorted:
    for category in bias_categories.keys():
        count = decade_category_counts[decade][category]
        category_trends[category].append(count)

# Plot
plt.figure(figsize=(12, 6))
for category, counts in category_trends.items():
    plt.plot(decades_sorted, counts, label=category.capitalize(), marker='o')

plt.title("Trends of Female Adjective Bias Categories Over Time")
plt.xlabel("Decade")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
