
# 🌍 GDP Growth Prediction using Machine Learning

This project explores the use of **machine learning models** to predict **GDP growth rates** of countries using a range of **macroeconomic indicators**. By leveraging historical data from the **World Bank's World Development Indicators (WDI)**, the aim is to build a predictive system that can offer insights into how economic factors correlate and influence a nation's economic growth.

---

## 📌 Project Objective

To develop a robust machine learning model that predicts the **annual GDP growth (%)** of countries using features such as:

- Inflation (Consumer Price Index)
- Unemployment Rate
- Gross Capital Formation
- Final consumption growth
- Trade openness
- Foreign Direct Investment (FDI)
- Sector Growth
- GDP Growth lag1
- GDP Growth lag2
- Export & Import growth
- Others...


---

## 🧠 Why This Project Matters

Understanding GDP growth is crucial for:
- Governments to design effective fiscal and monetary policies
- Investors to assess economic health and market potential
- Researchers to study long-term economic trends

By predicting GDP growth, we help stakeholders make informed decisions and reduce uncertainty.

---

## 📊 Dataset Description

- **Source:** [World Bank Open Data (WDI)](https://databank.worldbank.org/source/world-development-indicators)
- **Years Covered:** 1960 to 2023
- **Countries:** 200+ countries globally
- **Features:** 10+ macroeconomic indicators
- **Target Variable:** `GDP Growth (annual %)` — indicator code `NY.GDP.MKTP.KD.ZG`

---

## ⚙️ Technologies Used

- **Python**
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib / Seaborn** – Data visualization
- **scikit-learn** – Machine Learning algorithms
- **World Bank API (wbdata / pandas_datareader)** – Data fetching

---

## 🛠️ Workflow

### 1. **Data Collection**
- Collected indicators from World Bank via API.
- Unified them into a single DataFrame indexed by `Country`, `Year`.

### 2. **Data Preprocessing**
- Visualised and handled **missing data** via visual analysis and imputation.
- Detected(using boxplot) and handled **outliers**(using IQR, capping).
- Used forward-fill & backward-fill per country group.
- Detected and removed **outliers**.

### 3. **Exploratory Data Analysis**
- Visualized trends per country (e.g., India, USA, China).
- Examined correlation heatmaps between features and target.
- Identified important predictive patterns.

### 4. **Feature Engineering**
- Create new features.
- Normalized or scaled skewed features.
- Selected most relevant features using correlation and domain logic.

### 5. **Modeling**
- Applied baseline models: **Linear Regression**, **Ridge**, **Lasso**
- Tried advanced methods: **Random Forest Regressor**, **Gradient Boosting**, **XGBoosting**.
- Evaluated models with RMSE, MAE, and R² metrics.

### 6. **Prediction & Analysis**
- Visualized predictions vs. actual values.
- Compared performance across models and countries.
- Discussed economic interpretation of model results.

---

## 🔍 Key Findings

- Macroeconomic indicators can effectively predict GDP growth, especially with advanced ensemble models.
- XGBoost outperformed all other models with an R² of 0.9581 on the test set, indicating strong predictive power.
- Feature importance analysis revealed that factors like investment rate, exports, government spending, and inflation control had high predictive influence.
- Regularized models (Ridge/Lasso) performed better than plain linear regression, but tree-based models captured non-linearity more effectively.
- Regularized models (Ridge/Lasso) performed better than plain linear regression, but tree-based models captured non-linearity more effectively.
  
---

## 📈 Future Improvements

- Incorporate **non-linear models** like XGBoost, CatBoost.
- Explore **Time Series Forecasting** using LSTM or ARIMA.
- Introduce **categorical features** like income group or region.
- Develop an **interactive dashboard** to visualize trends dynamically.

---

## 🙌 Acknowledgements

- **World Bank** for providing open-access economic indicators.
- The **scikit-learn**, **statsmodels**, and **Seaborn** communities for excellent tools.
- Various research papers and documentation on economic modeling and forecasting.

---

## 💡 About Me

This project is a part of my journey to become a **Machine Learning Engineer**, with a special focus on understanding **economics through data**. I am passionate about combining **data science** with **real-world problems** to build practical and impactful solutions.

---

## 📬 Feedback & Contributions

Feel free to fork this repository, open issues, or contribute new features. Suggestions to improve model performance, add new economic indicators, or build visual dashboards are most welcome!

---

**Repository by:** yashnegi11 
**Project Title:** GDP Growth Prediction using ML  

