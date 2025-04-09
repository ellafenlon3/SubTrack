import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Subscription Analyzer", layout="centered")

st.title("📊 Student Subscription Analyzer")

# Read the uploaded Excel file
DATA_FILE = "Mock_Student_Subscription_Data Econometrics.xlsx"
import streamlit as st
import pandas as pd

# Banner
st.markdown("""
    <style>
    .block-container { padding-top: 0 !important; }
    .full-banner {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #82cbb2;
        color: white;
        padding: 1.2rem 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 1000;
        font-family: 'Segoe UI', sans-serif;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-bottom: 2px solid #66b3a6;
    }
    .top-left { display: flex; align-items: center; }
    .top-left img { height: 28px; margin-right: 10px; }
    .top-left h3 { margin: 0; font-size: 22px; font-weight: bold; }
    .top-center a {
        margin: 0 20px;
        text-decoration: none;
        color: white;
        font-weight: 500;
        font-size: 16px;
    }
    .top-center a:hover { text-decoration: underline; }
    .top-right { display: flex; align-items: center; }
    .user-circle {
        background-color: white;
        color: #82cbb2;
        border-radius: 50%;
        width: 35px;
        height: 35px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 14px;
        margin-right: 10px;
    }
    </style>

    <div class="full-banner">
        <div class="top-left">
            <img src="https://img.icons8.com/fluency/48/calendar.png"/>
            <h3>SubTrack</h3>
        </div>
        <div class="top-center">
            <a href="#">Dashboard</a>
            <a href="#">My Subscriptions</a>
            <a href="#">Analytics</a>
            <a href="#">Settings</a>
        </div>
        <div class="top-right">
            <div class="user-circle">GR</div>
            <span style="font-size: 15px;">Gerard Ryan</span>
        </div>
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

# Spacer
st.markdown("<br><br>", unsafe_allow_html=True)

# 📅 Upcoming Renewals (Styled like your screenshot)
st.markdown("""
<div style='
    background-color: #ffffff;
    border-radius: 12px;
    padding: 25px 30px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    max-width: 1000px;
    margin: 40px auto 0;
    font-family: "Segoe UI", sans-serif;
'>
    <h4 style='margin-bottom: 20px;'>Upcoming Renewals</h4>

    <div style='
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 12px;
        text-align: center;
        font-size: 14px;
        font-weight: 500;
        color: #333;
    '>
        <div>Mon</div>
        <div>Tue</div>
        <div>Wed</div>
        <div>Thu</div>
        <div>Fri</div>
        <div>Sat</div>
        <div>Sun</div>
    </div>

    <div style='
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 12px;
        text-align: center;
        margin-top: 12px;
        font-size: 14px;
        font-weight: 500;
    '>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>7</div>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>8</div>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>9</div>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>10</div>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>11</div>
        <div style='padding: 12px; background-color: #e7f6f1; border-radius: 8px; color: #197d66; font-weight: 600;'>12<br>FitnessPal</div>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>13</div>

        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>14</div>
        <div style='padding: 12px; background-color: #e7f6f1; border-radius: 8px; color: #197d66; font-weight: 600;'>15<br>Netflix</div>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>16</div>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>17</div>
        <div style='padding: 12px; background-color: #e7f6f1; border-radius: 8px; color: #197d66; font-weight: 600;'>18<br>Disney+</div>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>19</div>
        <div style='padding: 12px; background-color: #f9f9f9; border-radius: 8px;'>20</div>
    </div>
</div>
""", unsafe_allow_html=True)



