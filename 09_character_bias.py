from collections import defaultdict

# ✅ Step 1: Toy example character -> adjectives map
character_bias_map = {
    "Rohit": ["brave", "strong", "smart", "bold"],
    "Sonia": ["beautiful", "shy", "young", "slim"],
    "Amit": ["kind", "funny"],
    "Priya": ["caring", "pretty", "emotional", "loyal"]
}

# ✅ Step 2: Bias stereotype tags
stereotype_tags = {
    "Appearance": ["beautiful", "young", "pretty", "cute", "sexy", "hot", "attractive", "gorgeous", "slim", "fair"],
    "Agency": ["brave", "independent", "strong", "smart", "bold", "determined", "rebellious"],
    "Emotion": ["emotional", "caring", "kind", "sensitive", "loving", "loyal"],
    "Relationship": ["wife", "mother", "daughter", "girlfriend", "sister", "lover"],
}

# ✅ Step 3: Bias Detector Function
def detect_bias(adjectives):
    tag_scores = {tag: 0 for tag in stereotype_tags}
    for word in adjectives:
        for tag, keywords in stereotype_tags.items():
            if word in keywords:
                tag_scores[tag] += 1
    top_tag = max(tag_scores, key=tag_scores.get)
    if tag_scores[top_tag] == 0:
        return "No major stereotype tag detected.", []
    else:
        relevant_words = [w for w in adjectives if w in stereotype_tags[top_tag]]
        return f"High in {top_tag}", relevant_words

# ✅ Step 4: Generate Report
summary_output = "📊 Character-Level Bias Summary (Dynamic):\n\n"

for character, adjectives in character_bias_map.items():
    bias, tagged = detect_bias(adjectives)
    summary_output += f"Character: {character}\n"
    summary_output += f"Bias: {bias}\n"
    if tagged:
        summary_output += f"Tagged Adjectives: {tagged}\n"
    summary_output += "\n"

# ✅ Step 5: Save to file
with open("character_bias_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_output)

print(summary_output)
print("✅ Summary saved to character_bias_summary.txt")
