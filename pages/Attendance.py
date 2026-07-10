import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Attendance",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Attendance Report")

# --------------------------
# Load Attendance
# --------------------------

if not os.path.exists("attendance.csv"):
    st.error("attendance.csv not found!")
    st.stop()

attendance = pd.read_csv("attendance.csv")

if attendance.empty:
    st.warning("No attendance records found.")
    st.stop()

# --------------------------
# Summary Cards
# --------------------------

c1, c2 = st.columns(2)

c1.metric(
    "📋 Total Records",
    len(attendance)
)

c2.metric(
    "👤 Unique Students",
    attendance["Name"].nunique()
)

st.divider()

# --------------------------
# Search Student
# --------------------------

search = st.text_input(
    "🔍 Search Student"
)

if search:

    attendance = attendance[
        attendance["Name"].str.contains(
            search,
            case=False
        )
    ]

# --------------------------
# Date Filter
# --------------------------

dates = ["All"] + sorted(
    attendance["Date"].astype(str).unique().tolist()
)

selected = st.selectbox(
    "📅 Filter by Date",
    dates
)

if selected != "All":

    attendance = attendance[
        attendance["Date"] == selected
    ]

st.divider()

# --------------------------
# Attendance Table
# --------------------------

st.dataframe(
    attendance,
    use_container_width=True,
    hide_index=True
)

st.divider()

# --------------------------
# Download CSV
# --------------------------

csv = attendance.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="📥 Download Attendance CSV",
    data=csv,
    file_name="attendance.csv",
    mime="text/csv",
    use_container_width=True
)

st.divider()

# --------------------------
# Today's Attendance
# --------------------------

st.subheader("📅 Attendance Summary")

summary = attendance.groupby(
    "Date"
).size().reset_index(name="Students")

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)