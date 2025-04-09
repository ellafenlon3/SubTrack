import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Subscription Analyzer", layout="centered")

st.title("🎓SubTrack")

# Read the uploaded Excel file
DATA_FILE = "Mock_Student_Subscription_Data Econometrics.xlsx"
import streamlit as st
import pandas as pd

# Initialize session state variable
if "show_upgrade" not in st.session_state:
    st.session_state.show_upgrade = False


import streamlit as st

# --- Session state setup ---
if "upgrade_mode" not in st.session_state:
    st.session_state.upgrade_mode = False

# --- UI: Main banner ---
st.markdown("""
<div style="background-color: #7DD6B6; padding: 10px; text-align: center;">
    <strong style="color: white;">Save up to 25% on your monthly subscriptions with SubTrack Premium – 
    <a href="#" onclick="window.location.href='/?upgrade=1'" style="color: white; text-decoration: underline;">Upgrade now</a></strong>
</div>
""", unsafe_allow_html=True)
# --- Red Upgrade Button ---
if st.button("🔥 Upgrade Now", key="upgrade_now_btn"):
    st.session_state.upgrade_mode = True


# --- Fix the error here ---
query_params = st.query_params  # ✅ This is the correct usage — not st.query_params()
upgrade_clicked = st.session_state.upgrade_mode or query_params.get("upgrade") == "1"

# --- If upgrade param is in URL, turn modal on ---
if query_params.get("upgrade") == "1":
    st.session_state.upgrade_mode = True

# --- UPGRADE MODAL ---
if upgrade_clicked:
    st.markdown("""
        <style>
            .overlay {
                position: fixed;
                top: 0; left: 0;
                width: 100vw; height: 100vh;
                background: rgba(0, 0, 0, 0.4);
                z-index: 999;
            }
            .modal {
                background-color: #7DD6B6;
                padding: 40px;
                border-radius: 12px;
                text-align: center;
                width: 350px;
                margin: 100px auto;
            }
            input {
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
                border-radius: 5px;
                border: none;
            }
        </style>
        <div class='overlay'>
            <div class='modal'>
                <form method='get'>
                    <button type='submit' style='background:none; border:none; color:white; cursor:pointer; text-align:left;'>
                        ⬅ Go Back to Home
                    </button>
                </form>
                <h2 style="color: white;">Upgrade Now</h2>
                <p style="color: white;">One-time payment of €10.99</p>
                <form>
                    <input type="text" name="name" placeholder="Name on Card">
                    <input type="text" name="card" placeholder="Card Number">
                    <div style="display: flex; gap: 10px;">
                        <input type="text" name="exp" placeholder="MM/YY">
                        <input type="text" name="cvc" placeholder="CVC">
                    </div>
                    <button type="submit" style="margin-top: 10px; background-color: white; color: #00A9B4; padding: 10px 20px; border: none; border-radius: 8px; cursor: pointer;">
                        💳 Pay Now
                    </button>
                </form>
            </div>
        </div>
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
    Subscription Tracker & Cancellation App
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style='
    background-color: #ffffff;
    border-radius: 10px;
    padding: 20px 25px;
    margin-top: 20px;
    margin-bottom: 30px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    font-family: "Segoe UI", sans-serif;
    font-size: 16px;
'>
  🎓 <strong>Meet SubTrack – your ultimate student sidekick for subscription sanity!</strong><br><br>
  From Netflix to gym memberships, keep track of every subscription in one place, get alerts before free trials end, and cancel what you don’t use (finally 😅).<br><br>
  Built for busy students who’d rather binge shows than budgets – SubTrack saves time, money, and stress!
</div>
""", unsafe_allow_html=True)

import streamlit as st
import streamlit as st
import streamlit as st
import streamlit as st

# In the Dashboard section (replace/add as needed)

col1, col2 = st.columns([1, 3])

import streamlit as st
import streamlit as st

# Warning Box
st.markdown("""
<div style='
    background-color: #fdecea;
    border-left: 5px solid #f44336;
    padding: 16px;
    border-radius: 8px;
    margin-top: 20px;
'>
    <span style='font-size: 18px;'>⚠️ <strong>Forgotten Subscription Detected!</strong></span>
    <p style='margin: 8px 0 0 28px; font-size: 15px;'>
        You haven’t used your Spotify Premium subscription in 3 months but are still paying €9.99/month.
    </p>
</div>
""", unsafe_allow_html=True)
import streamlit as st

# --- 1. Setup session state ---
if "confirm_cancel" not in st.session_state:
    st.session_state.confirm_cancel = False


# --- 2. Confirm screen if cancel was clicked ---
if st.session_state.confirm_cancel:
    # Styled confirmation block
    st.markdown("""
        <div style='
            background-color: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            text-align: center;
            margin-top: 60px;
        '>
            <h2 style='color: #333;'>⚠️ Are you sure you want to cancel?</h2>
        </div>
    """, unsafe_allow_html=True)

    # Two buttons
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("🔙 Go Back"):
            st.session_state.confirm_cancel = False  # Return to main screen

    with col2:
        if st.button("✅ Yes, Cancel"):
            st.success("Subscription has been cancelled.")  # You can add logic here
            st.session_state.confirm_cancel = False  # Return to main screen after confirmation


# --- 3. Normal page content (when not confirming) ---
else:
    

    # Cancel button to trigger confirmation
    if st.button("Cancel Subscription"):
        st.session_state.confirm_cancel = True


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
import streamlit as st
import pandas as pd

# --- Initialize session state ---
if "subscription_data" not in st.session_state:
    st.session_state.subscription_data = pd.DataFrame({
        "Service": ["Netflix", "Spotify Premium", "Disney+", "Adobe Creative Cloud", "Xbox Game Pass", "FitnessPal Pro"],
        "Category": ["Entertainment", "Music", "Entertainment", "Education", "Gaming", "Fitness"],
        "Monthly Cost (€)": [14.99, 9.99, 8.99, 19.99, 9.99, 4.99],
        "Usage (hrs)": [12.5, 0.0, 4.2, 5.8, 0.0, 3.2],
        "Status": ["Active", "Forgotten", "Active", "Active", "Forgotten", "Active"],
        "Next Billing": ["Apr 15, 2025", "Apr 22, 2025", "Apr 18, 2025", "Apr 30, 2025", "Apr 27, 2025", "Apr 12, 2025"]
    })

if "show_add_form" not in st.session_state:
    st.session_state.show_add_form = False

# --- Toggle to show form ---
if not st.session_state.show_add_form:
    st.markdown("### 📄 Your Subscriptions")
    st.dataframe(st.session_state.subscription_data, use_container_width=True)

    if st.button("➕ Add New Subscription"):
        st.session_state.show_add_form = True

else:
    st.markdown("### ➕ Add New Subscription")

    service = st.text_input("Service")
    category = st.text_input("Category")
    monthly_cost = st.number_input("Monthly Cost (€)", min_value=0.0, step=0.01)
    usage = st.number_input("Usage (hrs)", min_value=0.0, step=0.1)
    status = st.selectbox("Status", ["Active", "Forgotten"])
    next_billing = st.text_input("Next Billing (e.g. Apr 30, 2025)")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("✅ Add"):
            if service and category and next_billing:
                new_row = {
                    "Service": service,
                    "Category": category,
                    "Monthly Cost (€)": monthly_cost,
                    "Usage (hrs)": usage,
                    "Status": status,
                    "Next Billing": next_billing
                }
                st.session_state.subscription_data.loc[len(st.session_state.subscription_data)] = new_row
                st.success(f"{service} added successfully!")
                st.session_state.show_add_form = False
            else:
                st.warning("Please fill in all required fields.")

    with col2:
        if st.button("🔙 Go Back"):
            st.session_state.show_add_form = False


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
import streamlit as st
