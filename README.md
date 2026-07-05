# 🇧🇩 Bangladesh Product Intelligence

An AI-powered product research engine for the Bangladesh eCommerce market.

The system researches products from online marketplaces, cleans the data, groups similar products into families, analyzes market demand, competition, saturation, seasonality, and generates an intelligent recommendation for product selection.

---

# Features

- Smart Keyword Expansion
- Product Search
- Product Cleaning
- Duplicate Removal
- Product Family Detection
- Demand Analysis
- Competition Analysis
- Market Saturation Analysis
- Evergreen Product Detection
- Seasonal Product Detection
- Price Analysis
- Product Ranking
- Intelligent Product Recommendation

---

# Project Structure

```
AI_PRODUCT_RESEARCH/

│
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── LICENSE
│
├── core/
├── database/
├── intelligence/
├── reports/
├── research/
├── tests/
├── docs/
├── data/
└── ui/
```

---

# Installation

Clone the repository

```bash
git clone <repository_url>
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install packages

```bash
pip install -r requirements.txt
```

---

# Run

```bash
python app.py
```

---

# Example

```
Enter Product Keyword

mini blender
```

Output

```
Products Found      : 194
Relevant Products   : 75
Unique Products     : 67
Recognized Products : 67

Family         : Mini Blender
Listings       : 67
Total Sold     : 1528
Demand         : 100
Competition    : 40
Saturation     : 40
Final Score    : 71
Recommendation : GOOD ⭐⭐⭐
```

---

# Intelligence Modules

- Demand Engine
- Competition Engine
- Saturation Engine
- Evergreen Engine
- Seasonal Engine
- Price Engine
- Final Ranking Engine
- Product Decision Engine

---

# Version

Current Version

```
v1.0
```

---

# Roadmap

## Version 1.1

- Facebook Marketplace Research
- Pickaboo Research
- Ryans Research
- StarTech Research
- Google Trends Integration
- Interactive Dashboard
- Charts
- CSV Export
- Excel Export
- AI Summary

---

# License

MIT License