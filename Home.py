import time
import streamlit as st
from PIL import Image
def run():
    st.title("Welcome to Snake Ladder Game")
    st.write("""
# Team 1 Project
""")
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #000000; /* Black color */
            color: #ffffff; /* Optional: Set text color to white for better contrast */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    img=Image.open("C:\\Users\\ANKIT KUMAR\\Downloads\\crown")
    st.image(img,width=1000)
    st.write("""
## *You are born to win, but to be a winner, you must plan to win, prepare to win, and expect to win.*""")
