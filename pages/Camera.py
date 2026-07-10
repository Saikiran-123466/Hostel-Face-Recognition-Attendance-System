import streamlit as st
from streamlit_webrtc import VideoProcessorBase, webrtc_streamer
import av
import cv2

from face_engine import recognize_frame, mark_attendance

st.set_page_config(
    page_title="AI Face Recognition Camera",
    page_icon="📷",
    layout="wide"
)

st.title("📷 AI Face Recognition Camera")

st.info("Show your face to the camera. Attendance will be marked automatically.")

# Prevent duplicate attendance during one session
marked_names = set()


class VideoProcessor(VideoProcessorBase):

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        results = recognize_frame(img)

        for (top, right, bottom, left), name in results:

            # Choose rectangle color
            if name == "Unknown":
                color = (0, 0, 255)
            else:
                color = (0, 255, 0)

            # Draw rectangle
            cv2.rectangle(
                img,
                (left, top),
                (right, bottom),
                color,
                2
            )

            # Display student name
            cv2.putText(
                img,
                name,
                (left, top - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            # Mark attendance
            if name != "Unknown":

                if name not in marked_names:

                    saved = mark_attendance(name)

                    if saved:
                        print(f"✅ Attendance Saved : {name}")

                    marked_names.add(name)

        return av.VideoFrame.from_ndarray(
            img,
            format="bgr24"
        )


webrtc_streamer(
    key="camera",
    video_processor_factory=VideoProcessor,
    media_stream_constraints={
        "video": True,
        "audio": False
    }
)

st.divider()

st.success("✅ Camera Ready")

st.markdown("""
### Instructions

- Click **START**
- Allow Camera Permission
- Look at the Camera
- Wait for your name to appear
- Attendance will be saved automatically
""")