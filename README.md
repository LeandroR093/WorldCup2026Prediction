# 🏆 World Cup 2026 Prediction Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-XGBoost%20%7C%20Scikit--Learn-orange.svg)
![Data Engineering](https://img.shields.io/badge/Data%20Engineering-AWS%20S3%20%7C%20Pandas-yellow.svg)
![Deployment](https://img.shields.io/badge/Deployment-Streamlit-red.svg)

## 📌 Project Overview
An end-to-end Machine Learning pipeline designed to predict the outcomes of the FIFA World Cup 2026 matches. This project goes beyond simple classification by utilizing probabilistic forecasting and Monte Carlo simulations to predict tournament brackets, goal differences, and overall tournament winners based on historical data.

This repository demonstrates a complete Data Science lifecycle: from data extraction and engineering to model training and interactive deployment.

## 🏗️ Architecture & Pipeline
The project is structured into four main phases:

1. **Data Ingestion & Engineering:** Extraction of historical international football match results, FIFA rankings, and team statistics. Raw and processed datasets are managed and stored using AWS S3 buckets.
2. **Exploratory Data Analysis (EDA) & Feature Engineering:** Creation of custom predictive features (e.g., winning streaks, goal differentials, offensive/defensive strength weights) using Pandas and NumPy.
3. **Predictive Modeling:** Implementation of robust tree-based models (XGBoost / Random Forest) to output both match outcome probabilities and expected goal differences.
4. **Deployment:** An interactive web application built with Streamlit, allowing users to simulate matches and explore the feature importance behind the model's decisions.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing & EDA:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning:** Scikit-learn, XGBoost
* **Cloud & Storage:** AWS S3, Boto3
* **Web App / Deployment:** Streamlit

## 🚀 How to Run Locally

1. **Clone the repository:**
```bash
   git clone [https://github.com/LeandroR093/WorldCup2026Prediction.git](https://github.com/LeandroR093/WorldCup2026Prediction.git)
   cd WorldCup2026Prediction
```
2. **Create a virtual environment:**
```bash
   python -m venv venv
   source venv/bin/activate
```
3. **Install dependencies:**
```bash
   pip install -r requirements.txt
```
4. **Run the Streamlit app:**
```bash
   streamlit run app/main.py
```

## 🗺️ Roadmap
- [x] Repository setup and architecture planning.
- [ ] Phase 1: Data extraction and AWS S3 integration.
- [ ] Phase 2: Feature engineering and historical backtesting (testing on the 2022 World Cup).
- [ ] Phase 3: Model training and hyperparameter tuning.
- [ ] Phase 4: Streamlit dashboard deployment.

## 👨‍💻 Author
Leandro Roldan

Junior Data Scientist

Connect with me on [LinkedIn](https://www.linkedin.com/in/leandro-roldan93)

