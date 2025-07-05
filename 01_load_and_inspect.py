import pandas as pd

# Load CSV files
female_verb = pd.read_csv("data/female_verb.csv")
female_adj = pd.read_csv("data/female_adjectives.csv")
male_verb = pd.read_csv("data/male_verb.csv")
male_adj = pd.read_csv("data/male_adjectives.csv")

# Sample print from raw CSVs
print("\n🔎 Sample raw male verbs (original):")
print(male_verb["verbs"].head(10).tolist())

print("\n🔎 Sample raw male adjectives (original):")
print(male_adj["adjectives"].head(10).tolist())

print("\n🔎 Sample raw female verbs (original):")
print(female_verb.head(10))

print("\n🔎 Sample raw female adjectives (original):")
print(female_adj.head(10))

# Show info and missing value stats
print("\n📌 Female Adjectives - Info:")
print(female_adj.info())
print("\n🧹 Missing values in Female Adjectives:")
print(female_adj.isnull().sum())

print("\n📌 Female Verbs - Info:")
print(female_verb.info())
print("\n🧹 Missing values in Female Verbs:")
print(female_verb.isnull().sum())

print("\n📌 Male Adjectives - Info:")
print(male_adj.info())
print("\n🧹 Missing values in Male Adjectives:")
print(male_adj.isnull().sum())

print("\n📌 Male Verbs - Info:")
print(male_verb.info())
print("\n🧹 Missing values in Male Verbs:")
print(male_verb.isnull().sum())
