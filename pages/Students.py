import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(
    page_title="Students",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("👨‍🎓 Student Management")

# ----------------------------
# Session State
# ----------------------------
if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

# ----------------------------
# Load Students
# ----------------------------
if not os.path.exists("students.csv"):
    st.error("students.csv not found!")
    st.stop()

students = pd.read_csv("students.csv")

# ----------------------------
# Search
# ----------------------------
search = st.text_input(
    "🔍 Search Student by Name or Room Number"
)

if search:

    students = students[
        students["Name"].astype(str).str.contains(
            search,
            case=False
        ) |
        students["RoomNo"].astype(str).str.contains(
            search
        )
    ]

st.success(f"Total Students : {len(students)}")

st.divider()

# ----------------------------
# Student Cards
# ----------------------------
for index, row in students.iterrows():

    with st.container(border=True):

        col1, col2 = st.columns([1,3])

        image_path = None

        if os.path.exists("images"):

            for file in os.listdir("images"):

                if file.lower().startswith(
                    row["Name"].lower()
                ):

                    image_path = os.path.join(
                        "images",
                        file
                    )

                    break

        with col1:

            if image_path and os.path.exists(image_path):

                st.image(
                    image_path,
                    width=140
                )

            else:

                if os.path.exists("assets/no_photo.png"):

                    st.image(
                        "assets/no_photo.png",
                        width=140
                    )

        with col2:

            st.subheader(row["Name"])

            st.write(
                f"🏠 Room Number : {row['RoomNo']}"
            )

            c1, c2 = st.columns(2)

            if c1.button(
                "✏ Edit",
                key=f"edit{index}"
            ):

                st.session_state.edit_index = index

            if c2.button(
                "🗑 Delete",
                key=f"delete{index}"
            ):

                all_students = pd.read_csv(
                    "students.csv"
                )

                all_students = all_students[
                    all_students["Name"] != row["Name"]
                ]

                all_students.to_csv(
                    "students.csv",
                    index=False
                )

                if os.path.exists("images"):

                    for file in os.listdir("images"):

                        if file.lower().startswith(
                            row["Name"].lower()
                        ):

                            os.remove(
                                os.path.join(
                                    "images",
                                    file
                                )
                            )

                st.success(
                    f"{row['Name']} Deleted Successfully."
                )

                st.rerun()
# =====================================================
# EDIT STUDENT
# =====================================================

if st.session_state.edit_index is not None:

    st.divider()

    st.subheader("✏ Edit Student")

    all_students = pd.read_csv("students.csv")

    student = all_students.iloc[
        st.session_state.edit_index
    ]

    new_name = st.text_input(
        "Student Name",
        value=student["Name"]
    )

    new_room = st.text_input(
        "Room Number",
        value=str(student["RoomNo"])
    )

    if st.button("💾 Update Student"):

        old_name = student["Name"]

        all_students.at[
            st.session_state.edit_index,
            "Name"
        ] = new_name

        all_students.at[
            st.session_state.edit_index,
            "RoomNo"
        ] = new_room

        all_students.to_csv(
            "students.csv",
            index=False
        )

        # Rename student photos
        if os.path.exists("images"):

            for file in os.listdir("images"):

                if file.lower().startswith(old_name.lower()):

                    old_path = os.path.join(
                        "images",
                        file
                    )

                    extension = os.path.splitext(file)[1]

                    number = ""

                    base = os.path.splitext(file)[0]

                    if base.lower().startswith(old_name.lower()):

                        number = base[len(old_name):]

                    new_file = f"{new_name}{number}{extension}"

                    new_path = os.path.join(
                        "images",
                        new_file
                    )

                    os.rename(
                        old_path,
                        new_path
                    )

        st.success("✅ Student Updated Successfully!")

        st.session_state.edit_index = None

        st.rerun()