import streamlit as st
import pandas as pd

st.set_page_config(page_title="HRMS Portal", layout="wide")
st.image("asu_banner.jpg", use_column_width=True)
st.markdown(
    "<div style='text-align: center;'><img src='asu_banner.jpg' width='600'></div>",
    unsafe_allow_html=True
)
st.title("MyASU-Inspired HRMS Portal")

# Load users
try:
    df_users = pd.read_csv("users.csv")
except FileNotFoundError:
    st.error("🛑 'users.csv' not found. Please upload it.")
    st.stop()

# Login field
email = st.text_input("Enter your email to log in:")
user = df_users[df_users['email'] == email].squeeze() if email in df_users['email'].values else None

if user is not None:
    st.success(f"Welcome {user['name']}! You are logged in as {user['role']}.")

    role = user['role']
    st.sidebar.title("Navigation")

    if st.sidebar.button("Profile"):
        st.subheader("👤 Profile")
        st.write(user)

    if st.sidebar.button("Attendance") and role in ["student", "professor", "admin"]:
        st.subheader("📆 Attendance")
        st.write("Attendance dashboard here...")

    if st.sidebar.button("Payroll") and role in ["staff", "payroll_admin", "admin"]:
        st.subheader("💵 Payroll")
        st.write("Payroll data shown here...")

    if st.sidebar.button("Student Classes") and role in ["professor", "admin"]:
        st.subheader("📚 Student Classes")
        st.write("Class lists and student info...")

    if st.sidebar.button("Finances") and role in ["student", "admin"]:
        st.subheader("🏦 Finances")
        st.write("Fee info and payments...")

else:
    if email:
        st.error("Email not found in the system. Try again or check spelling.")