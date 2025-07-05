import pandas as pd
import ast

df = pd.read_csv("data/female_adjectives.csv")

print("🔍 First 10 raw entries in 'adjectives' column:")
print(df["adjectives"].head(10).tolist())

print("\n✅ After literal_eval conversion:")
for entry in df["adjectives"].head(10):
    try:
        result = ast.literal_eval(entry)
        print(f"{entry} --> {result} (Type: {type(result)})")
    except Exception as e:
        print(f"{entry} --> Error: {e}")
