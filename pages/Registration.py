import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Student Registration",
    page_icon="➕",
    layout="wide"
)

st.title("➕ Register New Student")

# -----------------------------
# Create students.csv if missing
# -----------------------------
if not os.path.exists("students.csv"):
    pd.DataFrame(
        columns=["Name", "RoomNo"]
    ).to_csv(
        "students.csv",
        index=False
    )

students = pd.read_csv("students.csv")

# -----------------------------
# Registration Form
# -----------------------------

name = st.text_input("👤 Student Name")

room = st.text_input("🏠 Room Number")

photo = st.file_uploader(
    "📷 Upload Student Photo",
    type=["jpg", "jpeg", "png"]
)

st.divider()

# -----------------------------
# Preview
# -----------------------------

if photo is not None:

    st.image(
        photo,
        width=220,
        caption="Photo Preview"
    )

st.divider()

# -----------------------------
# Register Button
# -----------------------------

if st.button(
    "💾 Register Student",
    use_container_width=True
):

    if name == "" or room == "" or photo is None:

        st.error("Please fill all details.")

    elif name.lower() in students["Name"].str.lower().values:

        st.warning("Student already exists!")

    else:

        if not os.path.exists("images"):
            os.makedirs("images")

        image_path = os.path.join(
            "images",
            f"{name}1.jpg"
        )

        with open(image_path, "wb") as f:
            f.write(photo.getbuffer())

        new_student = pd.DataFrame({
            "Name": [name],
            "RoomNo": [room]
        })

        students = pd.concat(
            [students, new_student],
            ignore_index=True
        )

        students.to_csv(
            "students.csv",
            index=False
        )

        st.success("✅ Student Registered Successfully!")

        st.balloons()

st.divider()

st.subheader("📋 Registered Students")

st.dataframe(
    students,
    use_container_width=True,
    hide_index=True
)