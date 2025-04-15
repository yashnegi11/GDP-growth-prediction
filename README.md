
# 🌍 GDP Growth Prediction using Machine Learning

This project explores the use of **machine learning models** to predict **GDP growth rates** of countries using a range of **macroeconomic indicators**. By leveraging historical data from the **World Bank's World Development Indicators (WDI)**, the aim is to build a predictive system that can offer insights into how economic factors correlate and influence a nation's economic growth.

---

## 📌 Project Objective

To develop a robust machine learning model that predicts the **annual GDP growth (%)** of countries using features such as:

- Inflation (Consumer Price Index)
- Unemployment Rate
- Gross Capital Formation
- Government Expenditure
- Current Account Balance
- Foreign Direct Investment (FDI)
- Total Reserves
- Broad Money (M2)
- Export & Import of Goods and Services
- Others...

This project also emphasizes **economic data preprocessing**, **visualizations**, and **interpretability** for policy analysis and forecasting.

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
- **Years Covered:** 2000 to 2022
- **Countries:** 100+ countries globally
- **Features:** 10+ macroeconomic indicators
- **Target Variable:** `GDP Growth (annual %)` — indicator code `NY.GDP.MKTP.KD.ZG`

---

## ⚙️ Technologies Used

- **Python**
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib / Seaborn** – Data visualization
- **scikit-learn** – Machine Learning algorithms
- **statsmodels** – Statistical modeling
- **World Bank API (wbdata / pandas_datareader)** – Data fetching

---

## 🛠️ Workflow

### 1. **Data Collection**
- Collected indicators from World Bank via API.
- Unified them into a single DataFrame indexed by `Country`, `Year`.

### 2. **Data Preprocessing**
- Renamed confusing indicator codes to readable names.
- Handled **missing data** via visual analysis, interpolation, and imputation.
- Used forward-fill & backward-fill per country group.
- Detected and removed **outliers**.

### 3. **Exploratory Data Analysis**
- Visualized trends per country (e.g., India, USA, China).
- Examined correlation heatmaps between features and target.
- Identified important predictive patterns.

### 4. **Feature Engineering**
- Checked multicollinearity.
- Normalized or scaled features where required.
- Selected most relevant features using correlation and domain logic.

### 5. **Modeling**
- Applied baseline models: **Linear Regression**, **Ridge**, **Lasso**
- Tried advanced methods: **Random Forest Regressor**, **Gradient Boosting**, etc.
- Evaluated models with RMSE, MAE, and R² metrics.

### 6. **Prediction & Analysis**
- Visualized predictions vs. actual values.
- Compared performance across models and countries.
- Discussed economic interpretation of model results.

---

## 🔍 Key Findings

- GDP Growth is highly correlated with variables like **Capital Formation**, **Government Spending**, and **Inflation**.
- Linear models worked well for stable economies, while ensemble methods captured complex behavior in volatile regions.
- Data quality and availability vary drastically between countries; careful imputation was crucial.

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

**Repository by:** [Your GitHub Username]  
**Project Title:** GDP Growth Prediction using ML  
**License:** MIT (or any license you prefer)
