import streamlit as st

st.set_page_config(
    page_title="AI Hostel Face Recognition",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
# 🏠 AI Hostel Face Recognition Attendance System
### 🤖 Smart Attendance Management using Artificial Intelligence
""")

st.divider()

# -----------------------------
# WELCOME
# -----------------------------
st.success("""
## 👋 Welcome Admin!

This project automatically recognizes students using AI Face Recognition
and marks attendance without any manual work.

Use the navigation menu on the left to access all modules.
""")

st.divider()

# -----------------------------
# QUICK ACTIONS
# -----------------------------
st.subheader("🚀 Quick Navigation")

c1, c2 = st.columns(2)

with c1:

    st.page_link(
        "pages/Dashboard.py",
        label="📊 Dashboard"
    )

    st.page_link(
        "pages/Students.py",
        label="👨‍🎓 Student Management"
    )

    st.page_link(
        "pages/Registration.py",
        label="➕ Student Registration"
    )

with c2:

    st.page_link(
        "pages/Camera.py",
        label="📷 Live Camera"
    )

    st.page_link(
        "pages/Attendance.py",
        label="📋 Attendance Report"
    )

st.divider()

# -----------------------------
# PROJECT FEATURES
# -----------------------------
st.subheader("✨ Project Features")

left, right = st.columns(2)

with left:

    st.info("""
🤖 AI Face Recognition

👨‍🎓 Student Registration

👥 Student Management

📷 Live Camera

📋 Automatic Attendance

🔍 Search Students
""")

with right:

    st.info("""
📊 Dashboard Analytics

📈 Attendance Statistics

📥 CSV Download

✏ Edit Students

🗑 Delete Students

⚡ Fast & Easy Interface
""")

st.divider()

# -----------------------------
# TECHNOLOGIES
# -----------------------------
st.subheader("🛠 Technology Stack")

st.markdown("""
- 🐍 Python
- 🎈 Streamlit
- 📷 OpenCV
- 😊 face_recognition
- 🐼 Pandas
- 📊 Plotly
- 💻 VS Code
""")

st.divider()

# -----------------------------
# HOW TO USE
# -----------------------------
st.subheader("📖 How to Use")

st.markdown("""
### Step 1
Register a student from **Student Registration**

### Step 2
Go to **Live Camera**

### Step 3
Face will be recognized automatically

### Step 4
Attendance will be saved automatically

### Step 5
View attendance from **Attendance Report**
""")

st.divider()

# -----------------------------
# PROJECT STATUS
# -----------------------------
st.subheader("✅ Project Status")

st.success("✔ Face Recognition Working")
st.success("✔ Camera Working")
st.success("✔ Student Registration Working")
st.success("✔ Student Management Working")
st.success("✔ Attendance Report Working")
st.success("✔ Dashboard Analytics Working")

st.divider()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("""
---
### 👨‍💻 Developed by Sai Kiran

**B.Tech CSM**

**AI Powered Hostel Face Recognition Attendance System**

ACE Engineering College
""")