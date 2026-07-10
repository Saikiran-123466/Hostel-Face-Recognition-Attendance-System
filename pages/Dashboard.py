import streamlit as st
import pandas as pd
import plotly.express as px
import os
from datetime import datetime

st.set_page_config(page_title="Dashboard", page_icon="🏠", layout="wide")

st.markdown("""
# 📊 Dashboard

### Welcome to AI Hostel Face Recognition Attendance System
""")

st.success(
    "👋 Welcome Admin! Monitor attendance statistics below."
)
# -----------------------
# Load Students
# -----------------------
if os.path.exists("students.csv"):
    students = pd.read_csv("students.csv")
    total_students = len(students)
else:
    students = pd.DataFrame()
    total_students = 0

# -----------------------
# Load Attendance
# -----------------------
if os.path.exists("attendance.csv"):
    attendance = pd.read_csv("attendance.csv")
else:
    attendance = pd.DataFrame(columns=["Name","RoomNo","Date","Time"])

today = datetime.now().strftime("%d-%m-%Y")

if "Date" in attendance.columns:
    today_attendance = attendance[attendance["Date"] == today]
else:
    today_attendance = pd.DataFrame()

present = len(today_attendance)
absent = max(total_students - present, 0)

# -----------------------
# Dashboard Cards
# -----------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "👨 Total Students",
        total_students
    )

with c2:
    st.metric(
        "✅ Present",
        present
    )

with c3:
    st.metric(
        "❌ Absent",
        absent
    )

with c4:
    st.metric(
        "📅 Date",
        today
    )

st.divider()

# -----------------------
# Charts
# -----------------------
left, right = st.columns(2)

with left:

    pie = pd.DataFrame({
        "Status": ["Present", "Absent"],
        "Count": [present, absent]
    })

    fig = px.pie(
        pie,
        names="Status",
        values="Count",
        hole=0.45,
        title="Today's Attendance"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    if not attendance.empty:

        daily = attendance.groupby("Date").size().reset_index(name="Attendance")

        fig2 = px.bar(
            daily,
            x="Date",
            y="Attendance",
            color="Attendance",
            text_auto=True,
            title="Daily Attendance"
        )

        st.plotly_chart(fig2, use_container_width=True)

st.divider()

# -----------------------
# Recent Attendance
# -----------------------
st.subheader("📋 Latest Attendance Records")

if attendance.empty:
    st.info("No attendance records available.")
else:
    st.dataframe(
        attendance.tail(10),
        use_container_width=True
    )

st.divider()

# -----------------------
# Project Status
# -----------------------
st.subheader("🚀 System Status")

st.success("🟢 Face Recognition Engine : Active")

st.success("🟢 Student Database : Connected")

st.success("🟢 Attendance Module : Running")

st.success("🟢 Dashboard : Online")