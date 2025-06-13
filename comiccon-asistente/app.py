
import streamlit as st
from PIL import Image
import base64
import os

st.set_page_config(page_title="Comic-Con Málaga", layout="centered")

def get_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_path):
    bin_str = get_base64(image_path)
    page_bg_img = f"""
    <style>
    .stApp {{
        background: linear-gradient(to bottom, #0f3c71 40%, #f8c226 60%);
        background-image: url('data:image/png;base64,{bin_str}');
        background-size: cover;
        background-position: top center;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("assets/comiccon_header.png")

st.markdown(f"""
    <div style='text-align: center; padding-top: 300px;'>
        <img src='data:image/png;base64,{get_base64("assets/comiccon_logo.png")}' width='180'/>
        <h1 style='color: white; font-family: sans-serif;'>Welcome to<br/>Bienvenidos a</h1>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 6])

with col1:
    st.image("assets/avatar.png", width=70)

with col2:
    st.markdown("""
    <div style='background-color: #0f3c71; padding: 10px 15px; border-radius: 10px; color: white; font-size: 16px;'>
        Hello! How can I assist you with the Comic-Con event?
    </div>
    <div style='font-size: 12px; color: #888; margin-top: 5px;'>2:34 PM</div>
    """, unsafe_allow_html=True)

st.markdown("""
<div style='background-color: #fdf2cc; padding: 10px 15px; border-radius: 10px; color: #222; width: fit-content; margin-top: 10px;'>
    What’s on the schedule for Sunday?
</div>
""", unsafe_allow_html=True)

st.text_input("Type your message...", key="user_input")
