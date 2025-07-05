# 📊 Gender Bias Analysis in Bollywood Plot Descriptions

This project investigates **gender bias** in Bollywood movie plots, with a current focus on **female character portrayals**. It analyzes adjectives and verbs used to describe female characters, tags them based on a custom bias taxonomy, and visualizes patterns across time.

---

## ✅ Brief Strategy

1. **Data Parsing & Cleaning**: Read and clean preprocessed CSVs containing adjective and verb lists for female characters.
2. **Frequency Analysis**: Count top-used words and identify recurring themes.
3. **Bias Categorization**: Assign each word to a stereotype tag like `appearance`, `emotion`, `relationship`, or `agency`.
4. **Visualization**: 
   - Bar charts of top adjectives/verbs
   - Line plots of bias trends across decades
5. **Reporting**: Print concise summaries of usage patterns and tag distributions.

> ⚠️ **Note**: While the structure supports both genders, this version includes **in-depth analysis only for female characters**. Male character analysis is scoped for future development.

---

## 🧠 Bias Taxonomy

Words are tagged using the following stereotype categories:

| Category     | Description                                      |
|--------------|--------------------------------------------------|
| Appearance   | Focuses on looks: `beautiful`, `young`, `fair`   |
| Emotion      | Expresses feelings: `angry`, `happy`, `shy`      |
| Relationship | Defined by roles: `wife`, `daughter`, `widowed`  |
| Agency       | Reflects action/decision: `brave`, `independent` |
| Other        | Neutral or uncategorized                         |

---

## 🧪 Sample Output

**Top Adjectives (Female):**

| Word        | Frequency | Tag         |
|-------------|-----------|-------------|
| young       | 240       | Appearance  |
| beautiful   | 120       | Appearance  |
| sister      | 95        | Relationship|
| widowed     | 75        | Relationship|

**Bias Distribution (Female):**

| Tag         | Count     | % Usage     |
|-------------|-----------|-------------|
| Appearance  | 310       | 21.3%       |
| Relationship| 205       | 14.1%       |
| Emotion     | 110       | 7.6%        |
| Agency      | 80        | 5.5%        |

_Visualizations_:  
- `gender_adjectives_bargraph.png` – Bar chart comparing adjective frequency  
- Trend line of appearance-tagged words over decades

---

## 🛠️ Tools Used

- **Python 3**
- **Pandas**, **Matplotlib**, **Seaborn**
- `ast.literal_eval` for parsing lists
- Manual taxonomy tagging via `stereotypes.py`

---

## 📌 How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/NAMITHA-L/Gender-Bias-Analysis.git
   cd Gender-Bias-Analysis
   
Install dependencies:
pip install -r requirements.txt

Run each step sequentially:

python 01_load_and_inspect.py
python 02_clean_data.py
python 03_count_word_frequencies.py
python 04_tag_stereotypes.py
python 05_compare_gender_words.py
python 06_trend_over_time.py
python 07_summary_report.py

🧩 Future Scope:

🔍 Male Bias Analysis: Extend all analysis pipelines to male data files (male_adjectives.csv, male_verb.csv) and compare gender portrayals.

📊 Normalized Metrics: Account for total word count and gender representation size.

📈 Dashboards: Build interactive dashboards using Jupyter or Streamlit.

🧹 Advanced Cleaning: Incorporate lemmatization and POS tagging for improved tagging accuracy.



This project is currently focused on female character analysis but lays the foundation for broader gender bias studies across both genders in Bollywood narratives.
