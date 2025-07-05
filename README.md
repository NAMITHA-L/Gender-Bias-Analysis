# 📊 Gender Bias Analysis in Bollywood Plot Descriptions

This project investigates **gender bias** in Bollywood movie plots, currently focusing on **female character portrayals**. It analyzes adjectives and verbs, tags them with a bias taxonomy, and visualizes patterns across time.

---

## ✅ Brief Strategy

1. **Data Parsing & Cleaning**: Load and prepare female adjective/verb CSVs.
2. **Frequency Analysis**: Count and sort top-used descriptors.
3. **Bias Tagging**: Classify words into tags like `appearance`, `emotion`, `relationship`, `agency`.
4. **Visualization**: Bar charts and time trends of stereotype tags.
5. **Summary Reporting**: Concise bias breakdowns with tag distributions.

> ⚠️ Male character analysis is planned as part of future work.

---

## 🧠 Bias Taxonomy

| Tag          | Examples                   |
| ------------ | -------------------------- |
| Appearance   | beautiful, young, fair     |
| Emotion      | angry, shy, loving         |
| Relationship | wife, daughter, widowed    |
| Agency       | brave, independent, strong |
| Other        | Neutral/uncategorized      |

---

## 🧪 Sample Output

**Top Adjectives:**

| Word      | Count | Tag          |
| --------- | ----- | ------------ |
| young     | 240   | Appearance   |
| beautiful | 120   | Appearance   |
| sister    | 95    | Relationship |

**Bias Distribution:**

| Tag          | Count | % Usage |
| ------------ | ----- | ------- |
| Appearance   | 310   | 21.3%   |
| Relationship | 205   | 14.1%   |

*Visuals*:

* `gender_adjectives_bargraph.png`
* Time trend plots of appearance/emotion tags

---

## 🛠️ Tools Used

* Python, Pandas, Matplotlib, Seaborn
* `ast.literal_eval`, custom tagging logic (`stereotypes.py`)

---

## ▶️ How to Run

```bash
git clone https://github.com/NAMITHA-L/Gender-Bias-Analysis.git
cd Gender-Bias-Analysis
pip install -r requirements.txt
```

Then run scripts in order:

```bash
python 01_load_and_inspect.py
python 02_clean_data.py
python 03_count_word_frequencies.py
python 04_tag_stereotypes.py
python 05_compare_gender_words.py
python 06_trend_over_time.py
python 07_summary_report.py
```

---

## 🧹 Future Scope

* **🔄 GPT Rewrite**: Bias-free sentence rewriting using OpenAI models (`08_rewrite_bias.py`)
* **📝 Report Export**: Convert summaries to HTML/PDF (`09_export_report.py`)
* **🧽 Character-Level Tags**: Map adjectives/verbs to individual characters (`character_bias.py`)
* **☁️ Word Clouds**: Visualize stereotype tags as word clouds (`tag_cloud.png`)
* **📊 Male Analysis**: Extend full pipeline to male character datasets
* **📀 Normalized Metrics**: Adjust for plot length and gender ratio
* **📈 Dashboards**: Build with Streamlit or Gradio
* **🧪 Advanced NLP**: Add POS tagging, lemmatization, NER
* **🖼️ Poster Bias (Stretch)**: Image-based gender representation analysis

---

This project forms a foundation for **scalable gender bias studies** in Indian cinema — textual and beyond.
