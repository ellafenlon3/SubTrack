import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Subscription Analyzer", layout="centered")

st.title("📊 Student Subscription Analyzer")

# Read the uploaded Excel file
DATA_FILE = "Mock_Student_Subscription_Data Econometrics.xlsx"
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
# Show logged-in user name at the bottom of the Dashboard tab
st.markdown("""
    <hr style='margin-top: 40px; margin-bottom: 10px;'>

    <div style='text-align: left; font-size: 16px; font-weight: 500; color: #333;'>
        👤 Logged in as: <span style='color: #2b6777;'>Gerard Ryan</span>
    </div>
""", unsafe_allow_html=True)

try:
    df = pd.read_excel(DATA_FILE)

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
tab1 = st.tabs(["📊 Dashboard"])
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
