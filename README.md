# 🌍 GDP Growth Prediction Dashboard using Machine Learning

This project uses **machine learning** to predict the **GDP growth rate** of countries based on various **macroeconomic indicators**. Leveraging historical data from the **World Bank's World Development Indicators (WDI)**, we built both a **predictive model** and an **interactive Streamlit dashboard** to visualize trends and forecast economic performance.

---

## 📌 Project Objective

Build a robust system that:
- Predicts **annual GDP growth (%)** using key macroeconomic indicators.
- Offers **interactive visualization** and **country comparison** through a web dashboard.

---

## 🔧 Key Features of the Dashboard

- 📉 Visualize **GDP vs Inflation trends** over time for each country.
- 🌐 Compare **GDP growth and inflation rates** across multiple countries.
- 📈 View **sector-wise growth trends** (Agriculture, Industry, Services).
- 🧮 **Predict GDP growth** based on custom macroeconomic inputs.
- 🚨 Highlight potential risks like high inflation or low GDP growth.

---

## 🎯 Indicators Used for Prediction

- Inflation (CPI)
- Final Consumption Growth
- Gross Capital Formation
- Exports & Imports Growth
- Agriculture, Industry, Services Growth
- GDP Lag (1-year, 2-year)
- Trade Openness
- FDI (Foreign Direct Investment)
- Others...

---

## 🧠 Why This Project Matters

Understanding and forecasting GDP growth is crucial for:
- Policymaking by governments
- Investment decisions by businesses
- Long-term planning by international agencies

Our model brings **data science** and **economics** together to reduce uncertainty and assist in **evidence-based decision making**.

---

## 📊 Dataset Details

- **Source:** [World Bank - WDI](https://databank.worldbank.org/source/world-development-indicators)
- **Years:** 1960–2023
- **Countries:** 200+ countries
- **Target:** `GDP Growth (%)` (NY.GDP.MKTP.KD.ZG)

---

## ⚙️ Technologies & Tools

- **Python**
- **Streamlit** – Dashboard
- **Pandas / NumPy** – Data handling
- **Plotly** – Interactive charts
- **scikit-learn** – Model building
- **Google Colab** – Model training
- **Joblib** – Model serialization

---

## 🛠️ ML Workflow

1. **Data Collection** – World Bank API → CSV  
2. **Preprocessing** – Imputation, scaling, outlier handling  
3. **Feature Engineering** – Lag features, sector ratios  
4. **Modeling** – Linear Regression, Random Forest, Gradient Boosting, XGBoost  
5. **Evaluation** – RMSE, R², MAE  
6. **Deployment** – Streamlit dashboard for real-time prediction  

---

## 🧪 Key Results

- 📊 **XGBoost** achieved highest performance with **R² ≈ 0.95**  
- 🌟 Top predictors: investment, inflation, exports, sectoral growth  
- 🚀 Ensemble methods (RF, XGB) outperformed linear models  
- ✅ Final model: **Gradient Boosting Regressor**

---

## 🌐 Live Demo

- 🔗 **Streamlit App:** [Open Dashboard](https://gdp-growth-prediction-6krnqus8qvujykbiebatrj.streamlit.app/)

---

## 🗂️ Project Structure

GDP-growth-prediction/
│
├── app.py # Streamlit dashboard app
├── models/ # Trained model (.pkl) and feature columns
├── data/ # Preprocessed CSV data
├── notebooks/ # Colab notebook for training
├── requirements.txt # Python dependencies
├── README.md # This file


---

## 📈 Future Improvements

- Add **forecasting** features (show dotted lines for 2024–2026)
- Integrate **LSTM or ARIMA** for time-series prediction
- Add **region-based filtering** (e.g., South Asia, EU)
- Enable **data upload** for user-specific projections

---

## 🙌 Acknowledgements

- World Bank Open Data API  
- scikit-learn and Streamlit teams  
- Community research on GDP forecasting  

---

## 💡 About Me

I'm on a mission to become a **Machine Learning Engineer** by solving real-world challenges using data. This project is part of my journey to apply AI in **economic analysis and policy forecasting**.

---

## 💬 Feedback & Contributions

Feel free to ⭐ star, fork, or contribute to this repo. Suggestions for improvement and PRs are highly appreciated!

---

**Author:** [@yashnegi11](https://github.com/yashnegi11)  
**Repo:** [GDP-growth-prediction](https://github.com/yashnegi11/GDP-growth-prediction)
