import streamlit as st
import base64
from functions import add_bg_from_local

add_bg_from_local('images/art4.jpg')


original_title = '<p style="color:Black; font-size: 50px; font-weight: bold">🧘Positions</p>'
st.markdown(original_title, unsafe_allow_html=True)

pose = st.text_input("What pose would you like to see?", value="Downward Dog")

photo_description = f'<p style="color:Black; font-size: 35px;">{pose}</p>'
st.markdown(photo_description, unsafe_allow_html=True)
st.image(f"images/{pose}.jpg")
