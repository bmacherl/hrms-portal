import streamlit as st
import pandas as pd

# ---- Page settings ----
st.set_page_config(page_title="HRMS Portal", layout="wide")

# ---- ASU Banner ----
st.image("asu_banner.jpg", use_container_width=True)

# ---- App Title ----
st.markdown("<h2 style='text-align: center;'>Welcome to MyASU-Inspired HRMS Portal</h2>", unsafe_allow_html=True)

# ---- Load users ----
@st.cache_data
def load_users():
    return pd.read_csv("users.csv")

df_users = load_users()

# ---- Login Section ----
st.subheader("🔐 Login")
email = st.text_input("Enter your ASU email to log in:")

if email:
    if email in df_users['email'].values:
        user = df_users[df_users['email'] == email].squeeze()
        st.success(f"Welcome {user['name']}! You are logged in as **{user['role']}**.")

        # Sidebar navigation
        st.sidebar.title("📂 Menu")
        role = user['role']

        if st.sidebar.button("Profile"):
            st.subheader("👤 Profile")
            st.write(user)

        if st.sidebar.button("Attendance") and role in ["student", "professor", "admin"]:
            st.subheader("📆 Attendance")

            attendance_option = st.radio("Choose an option:", ["Show Attendance for Now", "View Course-wise Attendance"])
             if attendance_option == "Show Attendance for Now":
                     view_type = st.radio("View by:", ["Day-wise", "Week-wise"])

                 if view_type == "Day-wise":
                     st.info("📅 Day-wise tracking is a work in progress.")

                 elif view_type == "Week-wise":
                     st.subheader("📊 Weekly Attendance Breakdown")

            # Sample attendance data (replace with live data from face recognition)
                     courses = {
                         "AI and Data Analytics": {"total_hours": 5, "classes": 2, "attended": 1},
                         "Logistics in Supply Chain": {"total_hours": 5, "classes": 2, "attended": 2}
                     }

                     for course, stats in courses.items():
                         st.markdown(f"**{course}**")
                         attendance_ratio = stats["attended"] / stats["classes"]
                         attended_hours = attendance_ratio * stats["total_hours"]

                         st.write(f"Total Hours: {stats['total_hours']}")
                         st.write(f"Attended Classes: {stats['attended']} / {stats['classes']}")
                         st.write(f"Attended Hours: {attended_hours:.1f}")

                         st.pyplot(pie_chart(attended_hours, stats["total_hours"] - attended_hours))

        if st.sidebar.button("Payroll") and role in ["staff", "payroll_admin", "admin"]:
            st.subheader("💵 Payroll")
            st.write("Payroll summary coming soon!")

        if st.sidebar.button("Finances") and role in ["student", "admin"]:
            st.subheader("🏦 Finances")
            st.write("Fee info and payments coming soon!")

    else:
        st.error("Email not found. Please try again or contact admin.")
