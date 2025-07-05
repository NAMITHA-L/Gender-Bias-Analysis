from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import os
import re

# Define helper: extract words from a cell using regex
def extract_words(cell):
    if not isinstance(cell, str):
        return []
    return [match.group().lower() for match in re.finditer(r"\b[a-zA-Z]{3,}\b", cell)]

# Flatten all words in a column
def get_word_list(df, column_name):
    all_words = []
    for cell in df[column_name]:
        all_words.extend(extract_words(cell))
    return all_words

# Load data
adj_df = pd.read_csv("data/female_adjectives.csv")
verb_df = pd.read_csv("data/female_verb.csv")

# Get word lists
adjective_words = get_word_list(adj_df, "adjectives")
verb_words = get_word_list(verb_df, "verbs")

# Combine for emotion detection
all_words = adjective_words + verb_words

# Simple emotion keywords to filter emotion words from dataset
emotion_keywords = [
    "emotional", "caring", "crying", "angry", "upset", "nervous",
    "happy", "loving", "sad", "joy", "fear", "hurt", "excited"
]

# Filter words by category using actual data
appearance_words = [w for w in adjective_words if w in ["beautiful", "sexy", "pretty", "young", "hot", "attractive", "lovely"]]
agency_words = [w for w in verb_words if w in ["strong", "brave", "decides", "leads", "runs", "fights", "wins", "saves"]]
emotion_words = [w for w in all_words if w in emotion_keywords]

# Output dir
os.makedirs("images", exist_ok=True)

def generate_wordcloud(word_list, filename, title):
    if not word_list:
        print(f"⚠️ Skipping {title} — no words found.")
        return

    word_freq = Counter(word_list)
    wc = WordCloud(
        background_color="white",
        width=800,
        height=400,
        color_func=lambda *args, **kwargs: "black",
        collocations=False
    ).generate_from_frequencies(word_freq)

    plt.figure(figsize=(8, 4))
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.title(title, fontsize=16)
    plt.tight_layout()
    plt.savefig(f"images/{filename}", dpi=150)
    plt.close()
    print(f"✅ Saved: images/{filename}")

# Generate tag clouds
generate_wordcloud(appearance_words, "appearance_tag_cloud.png", "Appearance Word Cloud")
generate_wordcloud(agency_words, "agency_tag_cloud.png", "Agency Word Cloud")
generate_wordcloud(emotion_words, "emotion_tag_cloud.png", "Emotion Word Cloud")
