import streamlit as st
from PIL import Image
import base64
from functions import add_bg_from_local

add_bg_from_local('images/art4 (1).jpg')

original_title = '<p style="color:Black; font-size: 40px;">👧👦👧👦Meet the Team</p>'
st.markdown(original_title, unsafe_allow_html=True)

image = Image.open('images/team_yogi.jpg')
st.image(image, caption='Team Yogi')

body = '<p style="color:Black; font-size: 25px;">Team YOGi</p>'
st.caption(body, unsafe_allow_html=True)



description = '<p style="color:Black; font-size: 15px;">Dolly, Ted, Victoria and Melvin</p>'
st.markdown(description, unsafe_allow_html=True)

page_bg_img =  """
    <style>

    [data-testid="stSidebarNav"] {
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;

    }
    [data-testid="stSidebar"] {
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat;

    }
    [data-testid="stAppViewContainer"] {
        background-position:center;
        background: url("https://images.immediate.co.uk/production/volatile/sites/25/2019/10/orion-nebula-1f25f22.jpg?quality=90&webp=true&crop=2px,101px,1019px,679px&resize=1024,683");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat

    }
    [data-testid="stHeader"] {
        background-colour:rgba(0,0,0,0);
        colour: white;
        opacity: 0

    }
    [data-testid="stToolbar"] {
        right: 2rem
    }
    </style>
"""
