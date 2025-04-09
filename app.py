import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .stApp {
        background-color: #f5f5f5;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Subscription Analyzer", layout="centered")

st.title("📊 Student Subscription Analyzer")

# Read the uploaded Excel file
DATA_FILE = "Mock_Student_Subscription_Data Econometrics.xlsx"
import streamlit as st
import pandas as pd

st.markdown("""
<div style='
    background-color: #7EC6AD;
    padding: 10px 0;
    text-align: center;
    color: white;
    font-weight: bold;
    font-family: "Segoe UI", sans-serif;
    font-size: 15px;
'>
    Save up to 25% on your monthly subscriptions with SubTrack Premium –
    <a href='#' style='color: white; text-decoration: underline;'>Upgrade now</a>
</div>
""", unsafe_allow_html=True)


# ✅ Padding below banner so content isn't hidden
st.markdown("""
    <style>
    .main {
        padding-top: 100px !important;
    }
    </style>
""", unsafe_allow_html=True)
# 1. Full-width banner (already in your file)

# 2. Spacing CSS to push down content
st.markdown("""
    <style>
    .main {
        padding-top: 100px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. 💬 Subtitle right under banner
st.markdown("""
<div style='text-align: center; font-size: 50px; color: #444; margin-top: 10px; margin-bottom: 10px; font-weight: bold;'>
    Subscription Tracker & cancellation app
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='
    background-color: #fdeaea;
    border-left: 5px solid #f44336;
    padding: 15px 20px;
    border-radius: 8px;
    margin: 30px auto 20px;
    max-width: 900px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
'>
    <div style='display: flex; align-items: center;'>
        <span style='font-size: 22px; margin-right: 15px;'>⚠️</span>
        <div>
            <p style='margin: 0; font-weight: bold; font-size: 18px;'>Forgotten Subscription Detected!</p>
            <p style='margin: 5px 0 10px; color: #444;'>You haven’t used your Spotify Premium subscription in 3 months but are still paying €9.99/month.</p>
            <button style='background-color: #f44336; color: white; padding: 8px 14px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; margin-right: 10px;'>Cancel Subscription</button>
            <button style='background-color: #f0f0f0; color: #333; padding: 8px 14px; border: none; border-radius: 5px; cursor: pointer;'>Remind Later</button>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# In the Dashboard section (replace/add as needed)

col1, col2 = st.columns([1, 3])

with col1:
    # 👤 Profile card
    st.markdown("""
        <div style='
            background-color: #f3faf8;
            padding: 15px 20px;
            border-radius: 10px;
            width: 100%;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
            font-family: "Segoe UI", sans-serif;
            margin-bottom: 20px;
        '>
            <h4 style='margin-top: 0;'>Your Profile</h4>
            <p style='margin: 4px 0;'>Age: 21</p>
            <p style='margin: 4px 0;'>Monthly Income: €1,200</p>
            <p style='margin: 4px 0;'>Total Subscriptions: 6</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # You can add cards, alerts, or metrics here
    pass

st.markdown("""
<div style='
    display: flex;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
    max-width: 100%;
    font-family: "Segoe UI", sans-serif;
'>

  <div style='flex: 1; min-width: 220px; background-color: #ffffff; border-radius: 12px; padding: 20px 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
    <p style='margin: 0; font-weight: 500; color: #444;'>Monthly Subscription Cost</p>
    <p style='margin: 10px 0 0; font-size: 24px; font-weight: bold;'>€48.99</p>
    <p style='margin: 5px 0 0; font-size: 13px; color: #e85d5d;'>+12% from last month</p>
  </div>

  <div style='flex: 1; min-width: 220px; background-color: #ffffff; border-radius: 12px; padding: 20px 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
    <p style='margin: 0; font-weight: 500; color: #444;'>Average Usage</p>
    <p style='margin: 10px 0 0; font-size: 24px; font-weight: bold;'>21.5 hrs</p>
    <p style='margin: 5px 0 0; font-size: 13px; color: #3cb371;'>+3.2 hrs from last month</p>
  </div>

  <div style='flex: 1; min-width: 220px; background-color: #ffffff; border-radius: 12px; padding: 20px 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
    <p style='margin: 0; font-weight: 500; color: #444;'>Active Subscriptions</p>
    <p style='margin: 10px 0 0; font-size: 24px; font-weight: bold;'>6</p>
    <p style='margin: 5px 0 0; font-size: 13px; color: #e85d5d;'>+1 from last month</p>
  </div>

  <div style='flex: 1; min-width: 220px; background-color: #ffffff; border-radius: 12px; padding: 20px 30px; box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
    <p style='margin: 0; font-weight: 500; color: #444;'>Savings Opportunity</p>
    <p style='margin: 10px 0 0; font-size: 24px; font-weight: bold;'>€17.99</p>
    <p style='margin: 5px 0 0; font-size: 13px; color: #444;'>From 2 unused services</p>
  </div>

</div>
""", unsafe_allow_html=True)



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


# 📊 Dashboard title with icon
st.markdown("""
<div style='
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 28px;
    font-weight: bold;
    margin-top: 40px;
    margin-bottom: 15px;
    font-family: "Segoe UI", sans-serif;
'>
    <img src="https://img.icons8.com/fluency/48/dashboard-layout.png" width="32"/>
    Dashboard
</div>
""", unsafe_allow_html=True)


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
    data = {
        "name": "Gerard",
        "age": 21
    }
except Exception as e:
    st.error(f"Something went wrong: {e}")


# Sample subscription data
data = {
    "Service": ["Netflix", "Spotify Premium", "Disney+", "Adobe Creative Cloud", "Xbox Game Pass", "FitnessPal Pro"],
    "Category": ["Entertainment", "Music", "Entertainment", "Education", "Gaming", "Fitness"],
    "Monthly Cost (€)": [14.99, 9.99, 8.99, 19.99, 9.99, 4.99],
    "Usage (hrs)": [12.5, 0.0, 4.2, 5.8, 0.0, 3.2],
    "Status": ["Active", "Forgotten", "Active", "Active", "Forgotten", "Active"],
    "Next Billing": ["Apr 15, 2025", "Apr 22, 2025", "Apr 18, 2025", "Apr 30, 2025", "Apr 27, 2025", "Apr 12, 2025"]
}

# Spacer
st.markdown("<br><br>", unsafe_allow_html=True)

# 🧪 Free Trial Tracker (Styled)
st.markdown("""
<div style='
    background-color: #ffffff;
    border-radius: 12px;
    padding: 20px 25px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    max-width: 1000px;
    margin: 40px auto;
    font-family: "Segoe UI", sans-serif;
'>
    <h4 style='margin-bottom: 15px;'>Free Trial Tracker</h4>
    <table style='width: 100%; border-collapse: collapse; font-size: 15px;'>
        <thead>
            <tr style='background-color: #f5f6f8; text-align: left;'>
                <th style='padding: 12px;'>Service</th>
                <th style='padding: 12px;'>Start Date</th>
                <th style='padding: 12px;'>End Date</th>
                <th style='padding: 12px;'>Days Left</th>
                <th style='padding: 12px;'>Will Convert To</th>
                <th style='padding: 12px;'>Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr style='border-top: 1px solid #eee;'>
                <td style='padding: 12px;'>Audible Premium</td>
                <td style='padding: 12px;'>Apr 1, 2025</td>
                <td style='padding: 12px;'>Apr 30, 2025</td>
                <td style='padding: 12px;'>22</td>
                <td style='padding: 12px;'>€14.99/month</td>
                <td style='padding: 12px;'>
                    <button style='
                        background-color: #b6eadf;
                        color: #1b7a63;
                        font-weight: bold;
                        border: none;
                        padding: 6px 12px;
                        border-radius: 6px;
                        margin-right: 8px;
                        cursor: pointer;
                    '>Set Reminder</button>
                    <button style='
                        background-color: #f76c6c;
                        color: white;
                        font-weight: bold;
                        border: none;
                        padding: 6px 12px;
                        border-radius: 6px;
                        cursor: pointer;
                    '>Cancel Now</button>
                </td>
            </tr>
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)


