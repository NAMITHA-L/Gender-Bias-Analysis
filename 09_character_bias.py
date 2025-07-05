import re
from collections import defaultdict

# --- Load actual output from Step 07 (e.g., gender_bias_report.txt)
with open("gender_bias_report.txt", "r", encoding="utf-8") as f:
    report_text = f.read()

# --- Extract character → adjectives dynamically
character_bias_map = defaultdict(list)

# Assumes blocks like: Character: Rohit\nAdjectives: brave, strong
character_blocks = re.findall(r"Character:\s*(\w+)[^\n]*\nAdjectives?:\s*([^\n]+)", report_text)

for name, adj_str in character_blocks:
    adjectives = [a.strip().lower() for a in adj_str.split(",") if a.strip()]
    character_bias_map[name] = adjectives

# --- Define stereotype tags
stereotype_tags = {
    "Appearance": ["beautiful", "young", "pretty", "cute", "sexy", "hot", "attractive", "gorgeous", "slim", "fair"],
    "Agency": ["brave", "independent", "strong", "smart", "bold", "determined", "rebellious"],
    "Emotion": ["emotional", "caring", "kind", "sensitive", "loving", "loyal"],
    "Relationship": ["wife", "mother", "daughter", "girlfriend", "sister", "lover"],
}

# --- Determine dominant tag
def get_dominant_tag(words):
    tag_scores = {tag: 0 for tag in stereotype_tags}
    for word in words:
        for tag, keywords in stereotype_tags.items():
            if word in keywords:
                tag_scores[tag] += 1
    max_tag = max(tag_scores, key=tag_scores.get)
    if tag_scores[max_tag] == 0:
        return "No major stereotype tag detected.", []
    else:
        tagged_words = [w for w in words if w in stereotype_tags[max_tag]]
        return f"High in {max_tag}", tagged_words

# --- Generate output
summary_output = "📊 Character-Level Bias Summary (Dynamic):\n\n"

for character, adjectives in character_bias_map.items():
    bias, tagged = get_dominant_tag(adjectives)
    summary_output += f"Character: {character}\n"
    summary_output += f"Bias: {bias}\n"
    if tagged:
        summary_output += f"Tagged Adjectives: {tagged}\n"
    summary_output += "\n"

# --- Print and save
print(summary_output)

with open("character_bias_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_output)

print("✅ Dynamic character bias summary saved to 'character_bias_summary.txt'")
