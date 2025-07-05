import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from xhtml2pdf import pisa
import markdown
import re

# --- Define stereotype categories
stereotype_tags = {
    "Appearance": ["beautiful", "young", "pretty", "cute", "sexy", "hot", "attractive", "gorgeous", "slim", "fair"],
    "Agency": ["brave", "independent", "strong", "smart", "bold", "determined", "rebellious"],
    "Emotion": ["emotional", "caring", "kind", "sensitive", "loving", "loyal"],
    "Relationship": ["wife", "mother", "daughter", "girlfriend", "sister", "lover"],
}

# --- Helper: Clean and flatten column
def clean_and_flatten(df, column):
    all_words = []
    for entry in df[column].dropna():
        if entry.strip() == "[]":
            continue
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

# --- Load CSVs
female_df = pd.read_csv("data/female_adjectives.csv")
male_df = pd.read_csv("data/male_adjectives.csv")

female_words = clean_and_flatten(female_df, "adjectives")
male_words = clean_and_flatten(male_df, "adjectives")

# --- Top words
top_female = Counter(female_words).most_common(10)
top_male = Counter(male_words).most_common(10)

# --- Tagging
female_tags = classify_words(female_words, stereotype_tags)
male_tags = classify_words(male_words, stereotype_tags)

# --- Bias Ratio
appearance_bias_ratio = 100 * female_tags["Appearance"] / max(1, len(female_words))

# --- Create summary text
summary_txt = "# Gender Bias Analysis Report\n\n"

summary_txt += "## Top 10 Female Adjectives\n"
for word, count in top_female:
    summary_txt += f"- {word}: {count}\n"

summary_txt += "\n## Top 10 Male Adjectives\n"
for word, count in top_male:
    summary_txt += f"- {word}: {count}\n"

summary_txt += "\n## Stereotype Tag Distribution (Female)\n"
for k, v in female_tags.items():
    summary_txt += f"- {k}: {v}\n"

summary_txt += "\n## Stereotype Tag Distribution (Male)\n"
for k, v in male_tags.items():
    summary_txt += f"- {k}: {v}\n"

summary_txt += f"\n## Appearance-related bias in female descriptors\n- {appearance_bias_ratio:.1f}%\n"

# --- Generate bar chart
all_keywords = sorted(set(dict(top_female).keys()).union(dict(top_male).keys()))
x = np.arange(len(all_keywords))
width = 0.35

female_counts = [dict(top_female).get(word, 0) for word in all_keywords]
male_counts = [dict(top_male).get(word, 0) for word in all_keywords]

plt.figure(figsize=(12, 6))
plt.bar(x - width/2, female_counts, width, label='Female', color='orange')
plt.bar(x + width/2, male_counts, width, label='Male', color='blue')

plt.xticks(x, all_keywords, rotation=45, ha='right')
plt.ylabel('Frequency')
plt.title('Top Adjectives by Gender')
plt.legend()
plt.tight_layout()
plt.savefig("gender_adjectives_bargraph.png", dpi=300)
plt.close()

# --- Append image to markdown
summary_md = summary_txt + "\n\n![Graph](gender_adjectives_bargraph.png)"

# --- Convert to HTML
html = markdown.markdown(summary_md)

# --- Wrap for xhtml2pdf
html_wrapped = f"""
<html>
<head><meta charset="UTF-8"></head>
<body>{html}</body>
</html>
"""

# --- Create PDF
with open("gender_bias_report.pdf", "wb") as pdf_file:
    pisa.CreatePDF(html_wrapped, dest=pdf_file)

print("✅ PDF report created dynamically from analysis results.")
