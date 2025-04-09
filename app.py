import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Subscription Analyzer", layout="centered")

st.title("📊 Student Subscription Analyzer")

# Read the uploaded Excel file
DATA_FILE = "Mock_Student_Subscription_Data Econometrics.xlsx"

try:
    df = pd.read_excel(DATA_FILE)

    st.success("Data loaded successfully!")

    st.subheader("🔍 Data Preview")
    st.write(df.head())

    # Average monthly subscription cost
    if 'total_monthly_subscription_cost' in df.columns:
        avg_cost = df['total_monthly_subscription_cost'].mean()
        st.metric("💰 Avg. Monthly Subscription Cost (€)", round(avg_cost, 2))

    # Percent of users who cancelled a subscription
    if 'cancelled_any_subscription' in df.columns:
        cancelled_pct = df['cancelled_any_subscription'].mean() * 100
        st.metric("❌ % Cancelled Subscriptions", f"{round(cancelled_pct, 1)}%")

    # Forgotten subscription
    if 'has_forgotten_subscription' in df.columns:
        forgotten_pct = df['has_forgotten_subscription'].mean() * 100
        st.metric("🧠 % Forgotten Subscriptions", f"{round(forgotten_pct, 1)}%")

    # Forecast chart (just an example for now)
    st.subheader("📈 Forecasted Subscription Cost (Next 6 Months)")
    base_cost = df['total_monthly_subscription_cost'].mean()
    months = list(range(1, 7))
    forecast_costs = [base_cost + i * 10 for i in months]

    fig, ax = plt.subplots()
    ax.plot(months, forecast_costs, marker='o')
    ax.set_title("Estimated Monthly Costs")
    ax.set_xlabel("Month")
    ax.set_ylabel("Cost (€)")
    ax.grid(True)
    st.pyplot(fig)

except Exception as e:
    st.error(f"⚠️ Error reading data: {e}")
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📋 My Subscriptions", "📈 Analytics", "⚙️ Settings"])

with tab1:
    st.header("Dashboard")
    st.write("Show key metrics, charts, or summaries here.")

with tab2:
    st.header("My Subscriptions")
    st.write("List subscriptions, allow filtering, user-level info.")

with tab3:
    st.header("Analytics")
    st.write("Display graphs, forgotten subs, usage insights, etc.")

with tab4:
    st.header("Settings")
    st.write("Personalization or mock user settings here.")
page = st.sidebar.radio("Navigation", ["Dashboard", "My Subscriptions", "Analytics", "Settings"])

if page == "Dashboard":
    st.header("📊 Dashboard")
    st.write("Show key metrics, charts, profile box here.")

elif page == "My Subscriptions":
    st.header("📋 My Subscriptions")
    st.write("List of all active and inactive subscriptions.")

elif page == "Analytics":
    st.header("📈 Analytics")
    st.write("Trends, forgotten subs, spending insights.")

elif page == "Settings":
    st.header("⚙️ Settings")
    st.write("Update preferences or profile.")





