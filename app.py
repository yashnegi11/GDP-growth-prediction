import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import math
from pathlib import Path

st.set_page_config(page_title="🌍 GDP Dashboard", layout="wide")

page = st.sidebar.selectbox(
    "📊 Select Dashboard",
    ["📈 GDP Growth Prediction (ML)", "📉 Historical GDP Explorer"]
)

# -------------------- PAGE 1: ML Prediction Dashboard --------------------
if page == "📈 GDP Growth Prediction (ML)":

    @st.cache_data
    def load_data():
        return pd.read_csv("data/gdp_preprocessed.csv")

    @st.cache_resource
    def load_model():
        return joblib.load("models/gradient_boosting_model.pkl")

    @st.cache_data
    def load_feature_columns():
        return joblib.load("models/feature_columns.pkl")

    df = load_data()
    model = load_model()
    feature_columns = load_feature_columns()

    st.title("📈 GDP Growth Prediction Dashboard")

    df.sort_values(['Country', 'Year'], inplace=True)
    df['Inflation YoY (%)'] = df.groupby('Country')['Inflation (CPI)'].pct_change() * 100
    latest_year = df['Year'].max()
    latest_data = df[df['Year'] == latest_year]

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
        )
        fig.update_traces(mode='lines+markers')
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
        )
        fig2.update_traces(mode='lines+markers')
        fig2.update_layout(hovermode='x unified')
        st.plotly_chart(fig2, use_container_width=True)

# -------------------- PAGE 2: Historical GDP Explorer --------------------
elif page == "📉 Historical GDP Explorer":

    @st.cache_data
    def get_gdp_data():
        DATA_FILENAME = Path(__file__).parent / 'data/gdp_data.csv'
        raw_gdp_df = pd.read_csv(DATA_FILENAME)
        gdp_df = raw_gdp_df.melt(
            ['Country Code'],
            [str(x) for x in range(1960, 2024)],
            'Year',
            'GDP',
        )
        gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])
        return gdp_df

    gdp_df = get_gdp_data()

    st.title("📉 Historical GDP Explorer")

    min_value = gdp_df['Year'].min()
    max_value = gdp_df['Year'].max()

    from_year, to_year = st.slider(
        'Select time range',
        min_value=min_value,
        max_value=max_value,
        value=[min_value, max_value]
    )

    countries = gdp_df['Country Code'].unique()

    selected_countries = st.multiselect(
        'Select countries to visualize',
        countries,
        ['IND', 'USA', 'CHN', 'PAK']
    )

    if not selected_countries:
        st.warning("Please select at least one country.")
    else:
        filtered_gdp_df = gdp_df[
            (gdp_df['Country Code'].isin(selected_countries))
            & (gdp_df['Year'] >= from_year)
            & (gdp_df['Year'] <= to_year)
        ]

        st.header('📈 GDP Over Time')
        st.line_chart(
            filtered_gdp_df,
            x='Year',
            y='GDP',
            color='Country Code',
        )

        st.header(f'📊 GDP in {to_year}')
        cols = st.columns(4)

        first_year = gdp_df[gdp_df['Year'] == from_year]
        last_year = gdp_df[gdp_df['Year'] == to_year]

        for i, country in enumerate(selected_countries):
            col = cols[i % len(cols)]
            with col:
                try:
                    first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1e9
                    last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1e9
                    growth = f'{last_gdp / first_gdp:,.2f}x'
                    delta_color = 'normal'
                except:
                    last_gdp = 0
                    growth = 'n/a'
                    delta_color = 'off'

                st.metric(
                    label=f'{country} GDP',
                    value=f'{last_gdp:,.0f}B',
                    delta=growth,
                    delta_color=delta_color
                )
