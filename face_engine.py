import cv2
import face_recognition
import pandas as pd
import numpy as np
import os
from datetime import datetime

# -----------------------------
# Load Students
# -----------------------------
students = pd.read_csv("students.csv")

known_face_encodings = []
known_face_names = []

DISTANCE_THRESHOLD = 0.45

# -----------------------------
# Load Known Faces
# -----------------------------
def load_known_faces():

    global known_face_encodings
    global known_face_names

    known_face_encodings.clear()
    known_face_names.clear()

    image_folder = "images"

    for file in os.listdir(image_folder):

        if file.lower().endswith((".jpg", ".jpeg", ".png")):

            path = os.path.join(image_folder, file)

            image = face_recognition.load_image_file(path)

            encodings = face_recognition.face_encodings(image)

            if len(encodings) == 0:
                continue

            known_face_encodings.append(encodings[0])

            filename = os.path.splitext(file)[0]

            if filename.lower().startswith("ajay"):
                person_name = "Ajay"

            elif filename.lower().startswith("saikiran"):
                person_name = "Saikiran"

            else:
                person_name = filename

            known_face_names.append(person_name)

# -----------------------------
# Recognize One Face
# -----------------------------
def recognize_face(face_encoding):

    name = "Unknown"

    if len(known_face_encodings) == 0:
        return name

    distances = face_recognition.face_distance(
        known_face_encodings,
        face_encoding
    )

    best_index = np.argmin(distances)

    if distances[best_index] < DISTANCE_THRESHOLD:
        name = known_face_names[best_index]

    return name

# -----------------------------
# Get Student Details
# -----------------------------
def get_student(name):

    row = students[
        students["Name"].str.lower() == name.lower()
    ]

    if row.empty:
        return None

    return row.iloc[0]

# -----------------------------
# Mark Attendance
# -----------------------------
def mark_attendance(name):

    student = get_student(name)

    if student is None:
        return False

    today = datetime.now().strftime("%d-%m-%Y")

    # Read attendance file
    if os.path.exists("attendance.csv"):
        attendance = pd.read_csv("attendance.csv")
    else:
        attendance = pd.DataFrame(
            columns=["Name", "RoomNo", "Date", "Time"]
        )

    # Check if already marked today
    already_marked = attendance[
        (attendance["Name"].str.lower() == name.lower()) &
        (attendance["Date"] == today)
    ]

    if not already_marked.empty:
        print(f"{name} already marked today.")
        return False

    now = datetime.now()

    new_row = pd.DataFrame({
        "Name": [name],
        "RoomNo": [student["RoomNo"]],
        "Date": [today],
        "Time": [now.strftime("%H:%M:%S")]
    })

    new_row.to_csv(
        "attendance.csv",
        mode="a",
        header=attendance.empty,
        index=False
    )

    print(f"Attendance Saved : {name}")

    return True

# -----------------------------
# Recognize Faces in a Frame
# -----------------------------
def recognize_frame(frame):

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)

    face_encodings = face_recognition.face_encodings(
        rgb,
        face_locations
    )

    results = []

    for face_encoding, face_location in zip(
        face_encodings,
        face_locations
    ):

        name = recognize_face(face_encoding)

        results.append(
            (face_location, name)
        )

    return results


# -----------------------------
# Load Faces Automatically
# -----------------------------
load_known_faces()

print("✅ Face Engine Ready")