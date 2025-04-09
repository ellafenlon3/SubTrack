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
import pandas as pd
import streamlit as st

# Sample subscription data
data = {
    "Service": ["Netflix", "Spotify Premium", "Disney+", "Adobe Creative Cloud", "Xbox Game Pass", "FitnessPal Pro"],
    "Category": ["Entertainment", "Music", "Entertainment", "Education", "Gaming", "Fitness"],
    "Monthly Cost (€)": [14.99, 9.99, 8.99, 19.99, 9.99, 4.99],
    "Usage (hrs)": [12.5, 0.0, 4.2, 5.8, 0.0, 3.2],
    "Status": ["Active", "Forgotten", "Active", "Active", "Forgotten", "Active"],
    "Next Billing": ["Apr 15, 2025", "Apr 22, 2025", "Apr 18, 2025", "Apr 30, 2025", "Apr 27, 2025", "Apr 12, 2025"]
}

df = pd.DataFrame(data)

# Show it on the dashboard
st.subheader("📋 Your Subscriptions")
st.dataframe(df, use_container_width=True)
import streamlit as st
import pandas as pd

# App setup
st.set_page_config(page_title="SubTrack", layout="wide")

# Top navigation (no sidebar)
page = st.radio(
    "Navigate to:",
    ["Dashboard", "My Subscriptions", "Analytics", "Settings"],
    horizontal=True,
    key="top_nav"
)

# Dashboard Tab
if page == "Dashboard":
    st.title("📊 Dashboard")
    st.subheader("📋 Your Subscriptions Overview")

    # Sample subscription data (edit as needed)
    data = {
        "Service": ["Netflix", "Spotify Premium", "Disney+", "Adobe Creative Cloud", "Xbox Game Pass", "FitnessPal Pro"],
        "Category": ["Entertainment", "Music", "Entertainment", "Education", "Gaming", "Fitness"],
        "Usage (hrs)": [12.5, 0.0, 4.2, 5.8, 0.0, 3.2],
        "Next Billing": ["Apr 15, 2025", "Apr 22, 2025", "Apr 18, 2025", "Apr 30, 2025", "Apr 27, 2025", "Apr 12, 2025"]
    }







