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

st.markdown("""
    <style>
    .profile-card {
        background-color: #f0f8f5;
        padding: 1rem;
        border-radius: 10px;
        width: 220px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-top: 20px;
        position: absolute;
        top: 100px;
        left: 20px;
        z-index: 1;
    }
    .profile-card h4 {
        margin-top: 0;
        color: #1b4332;
    }
    </style>

    <div class="profile-card">
        <h4>Your Profile</h4>
        <p>Age: 21</p>
        <p>Monthly Income: €1,200</p>
        <p>Total Subscriptions: 6</p>
    </div>
""", unsafe_allow_html=True)

