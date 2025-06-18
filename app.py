import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# Load data and model
@st.cache_data
def load_data():
    return pd.read_csv("gdp_preprocessed.csv")

@st.cache_resource
def load_model():
    return joblib.load("models/gradient_boosting_model.pkl")

@st.cache_data
def load_feature_columns():
    return joblib.load("models/feature_columns.pkl")

df = load_data()
model = load_model()
feature_columns = load_feature_columns()

st.title("🌍 GDP Growth Prediction Dashboard")

# Preprocess data
df.sort_values(['Country', 'Year'], inplace=True)
df['Inflation YoY (%)'] = df.groupby('Country')['Inflation (CPI)'].pct_change() * 100
latest_year = df['Year'].max()
latest_data = df[df['Year'] == latest_year]

# --- Country Selector ---
st.subheader("🌐 Country Overview")
country = st.selectbox("Select a country", sorted(df['Country'].unique()))
year = st.slider("Select Year", int(df['Year'].min()), int(df['Year'].max()), int(latest_year))
cols = [
    'Agriculture Growth (%)', 'Industry Growth (%)', 'Services Growth (%)',
    'Exports Growth (%)', 'Imports Growth (%)',
    'Final Consumption Growth (%)', 'Gross Capital Formation Growth (%)',
    'Inflation YoY (%)'
]

snapshot = df[(df['Country'] == country) & (df['Year'] == year)][cols].T
snapshot.columns = ['Value']
st.dataframe(snapshot.style.format("{:.2f}"))

st.divider()

# --- GDP vs Inflation Trend ---
st.subheader(f"📉 GDP vs Inflation Trend - {country}")
trend_df = df[df['Country'] == country]
fig_trend = px.line(
    trend_df,
    x='Year',
    y=['GDP Growth (%)', 'Inflation YoY (%)'],
    labels={"value": "Percent (%)", "variable": "Indicator"},
    title=f"GDP Growth vs Inflation YoY ({country})"
)
fig_trend.update_traces(mode='lines+markers')
st.plotly_chart(fig_trend, use_container_width=True)

st.divider()

# --- Sector-wise Growth Over Time ---
st.subheader(f"📈 Sector Growth Over Time - {country}")
sector_cols = ['Agriculture Growth (%)', 'Industry Growth (%)', 'Services Growth (%)']
fig_sector = px.line(
    trend_df,
    x='Year',
    y=sector_cols,
    title=f"Sector-wise GDP Growth ({country})",
    labels={"value": "Growth (%)", "variable": "Sector"}
)
st.plotly_chart(fig_sector, use_container_width=True)

st.divider()

# --- Multi-country GDP and Inflation Comparison ---
st.subheader("📊 Compare GDP Growth Across Countries")
countries = st.multiselect("Select countries", sorted(df['Country'].unique()), default=[country])

if countries:
    compare_df = df[df['Country'].isin(countries)]

    fig = px.line(
        compare_df,
        x="Year",
        y="GDP Growth (%)",
        color="Country",
        markers=True,
        title="GDP Growth Comparison",
        labels={"GDP Growth (%)": "GDP Growth (%)", "Year": "Year"},
    )
    fig.update_traces(mode='lines+markers', hovertemplate='Country: %{legendgroup}<br>Year: %{x}<br>GDP: %{y:.2f}%')
    fig.update_layout(hovermode='x unified')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("💹 Inflation Rate Comparison (YoY %)")
    fig2 = px.line(
        compare_df,
        x="Year",
        y="Inflation YoY (%)",
        color="Country",
        markers=True,
        title="Inflation Rate Comparison (YoY %)",
        labels={"Inflation YoY (%)": "Inflation Rate (%)", "Year": "Year"},
    )
    fig2.update_traces(mode='lines+markers', hovertemplate='Country: %{legendgroup}<br>Year: %{x}<br>Inflation: %{y:.2f}%')
    fig2.update_layout(hovermode='x unified')
    st.plotly_chart(fig2, use_container_width=True)

from datetime import datetime

# Simulate forecast (replace with real model predictions if available)
forecast_years = [2024, 2025, 2026]  # Change based on your dataset
forecast_data = []

for c in countries:
    last_gdp = df[(df['Country'] == c) & (df['Year'] == df['Year'].max())]['GDP Growth (%)'].values[0]
    # Dummy logic: slight growth or decline (replace with model)
    for y in forecast_years:
        forecast_value = last_gdp * (1 + 0.01 * (y - 2023))  # Simple projection
        forecast_data.append({"Country": c, "Year": y, "GDP Growth (%)": forecast_value, "Data Type": "Forecast"})

# Add actual data type to existing data
actual_data = compare_df.copy()
actual_data["Data Type"] = "Actual"

# Combine actual + forecast
forecast_df = pd.DataFrame(forecast_data)
combined_df = pd.concat([actual_data, forecast_df])

# Plot with dashed lines for forecast
fig = px.line(
    combined_df,
    x="Year",
    y="GDP Growth (%)",
    color="Country",
    line_dash="Data Type",  # Solid vs Dash
    markers=True,
    title="GDP Growth Comparison (with Forecast)",
    labels={"GDP Growth (%)": "GDP Growth (%)", "Year": "Year"},
)

fig.update_traces(
    mode='lines+markers',
    hovertemplate='Country: %{legendgroup}<br>Year: %{x}<br>GDP: %{y:.2f}%',
)
fig.update_layout(hovermode='x unified')

st.plotly_chart(fig, use_container_width=True)
