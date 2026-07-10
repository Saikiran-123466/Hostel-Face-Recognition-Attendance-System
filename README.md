# 🏠 AI Hostel Face Recognition Attendance System

## 📌 Project Overview

The **AI Hostel Face Recognition Attendance System** is an intelligent attendance management application that automatically identifies students using face recognition and marks their attendance without manual intervention.

This system reduces paperwork, prevents proxy attendance, and provides a fast and accurate attendance management solution.

---

# 🎯 Objectives

- Automate hostel attendance using AI.
- Eliminate manual attendance registers.
- Prevent duplicate attendance.
- Manage student records efficiently.
- Generate attendance reports instantly.

---

# ✨ Features

- 🤖 AI Face Recognition
- 📷 Live Camera Detection
- ✅ Automatic Attendance Marking
- 🚫 Duplicate Attendance Prevention
- 👨‍🎓 Student Registration
- 👥 Student Management
- ✏️ Edit Student Details
- 🗑 Delete Student
- 🔍 Search Students
- 📊 Dashboard Analytics
- 📋 Attendance Report
- 📥 Download Attendance CSV
- 📈 Attendance Statistics

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| OpenCV | Camera Processing |
| face_recognition | Face Detection & Recognition |
| Pandas | Data Management |
| NumPy | Numerical Operations |
| Plotly | Dashboard Charts |

---

# 📂 Project Structure

```text
Hostel Attendance
│
├── app.py
├── face_engine.py
├── students.csv
├── attendance.csv
├── requirements.txt
│
├── images/
│
├── assets/
│
└── pages/
    ├── Dashboard.py
    ├── Students.py
    ├── Attendance.py
    ├── Camera.py
    └── Registration.py
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Saikiran-123466/Hostel-AI-Face-Recognition.git
```

Move into the project

```bash
cd Hostel-AI-Face-Recognition
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📖 How to Use

### Step 1

Register a student.

- Enter student name.
- Enter room number.
- Upload student photo.

---

### Step 2

Open the Camera page.

---

### Step 3

Allow camera permission.

---

### Step 4

The system recognizes the student's face automatically.

---

### Step 5

Attendance is saved automatically in **attendance.csv**.

---

### Step 6

View reports from the Attendance page.

---

# 📊 Dashboard

The dashboard displays:

- Total Students
- Present Students
- Absent Students
- Pie Chart Analytics
- Daily Attendance Bar Chart
- Recent Attendance

---

# 📷 Face Recognition Workflow

```
Student Registration
        │
        ▼
Upload Image
        │
        ▼
Face Encoding
        │
        ▼
Open Camera
        │
        ▼
Detect Face
        │
        ▼
Recognize Student
        │
        ▼
Mark Attendance
        │
        ▼
Save to attendance.csv
```

---



# 👨‍💻 Developer

**Sai Kiran**

B.Tech – Computer Science and Machine Learning (CSM)

ACE Engineering College

---

# 📜 License

This project is developed for educational purposes.

---

# ⭐ Acknowledgement

Thanks to the open-source Python community and the developers of Streamlit, OpenCV, face_recognition, Pandas, NumPy, and Plotly for providing the tools used in this project.