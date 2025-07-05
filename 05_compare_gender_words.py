from collections import Counter
import pandas as pd
import re
import matplotlib.pyplot as plt

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

def compare_top_words(female_words, male_words, label):
    female_counts = Counter(female_words)
    male_counts = Counter(male_words)

    # Get top 10 from each
    top_female = dict(female_counts.most_common(10))
    top_male = dict(male_counts.most_common(10))

    # Create unified list of all top words
    all_top_words = list(set(list(top_female.keys()) + list(top_male.keys())))
    
    # Prepare data for plotting
    female_vals = [top_female.get(word, 0) for word in all_top_words]
    male_vals = [top_male.get(word, 0) for word in all_top_words]

    # Plot
    x = range(len(all_top_words))
    plt.figure(figsize=(12, 6))
    plt.bar(x, female_vals, width=0.4, label='Female', align='center', alpha=0.7)
    plt.bar([i + 0.4 for i in x], male_vals, width=0.4, label='Male', align='center', alpha=0.7)
    plt.xticks([i + 0.2 for i in x], all_top_words, rotation=45)
    plt.title(f"Top {label}s: Female vs Male")
    plt.xlabel(f"{label.capitalize()}s")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Load files
female_adj = pd.read_csv("data/female_adjectives.csv")
male_adj = pd.read_csv("data/male_adjectives.csv")
female_verbs = pd.read_csv("data/female_verb.csv")
male_verbs = pd.read_csv("data/male_verb.csv")

# Clean
female_adj_words = clean_and_flatten(female_adj, "adjectives")
male_adj_words = clean_and_flatten(male_adj, "adjectives")
female_verb_words = clean_and_flatten(female_verbs, "verbs")
male_verb_words = clean_and_flatten(male_verbs, "verbs")

# Compare
compare_top_words(female_adj_words, male_adj_words, "adjective")
compare_top_words(female_verb_words, male_verb_words, "verb")
