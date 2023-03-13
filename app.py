import streamlit as st
import base64    #pip install pybase64
import streamlit.components.v1 as components
from PIL import Image
from functions import add_bg_from_local

st.set_page_config(
    page_title="Yogi",
    page_icon="🧘‍♂️",
)



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
        background: url("https://s32625.pcdn.co/wp-content/uploads/2020/08/Spring-Mist-oil-on-linen-20x24-Albert-Handell_WO-1536x1163.jpg.webp");
        background-size: cover;
        background-position: top left;
        background-repeat: no-repeat

    }
    [data-testid="stHeader"] {
        background-colour:rgba(0,0,0,0);
        colour: white;
        opacity: 0.1

    }
    [data-testid="stToolbar"] {
        right: 2rem
    }
    </style>
"""
# [data-testid="stSidebarNav"] {
#     background: url("https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/sacred-geometry-contemporary-art-metatrons-cube-dean-marston.jpg")
#     }
#
st.markdown(page_bg_img, unsafe_allow_html=True)

original_title = '<p style="font-family:Courier; color:white; font-size: 40px;">ॐ Yoga Pose Detection ॐ</p>'
st.markdown(original_title, unsafe_allow_html=True)

#st.title("")
st.sidebar.success("Select a page above.")

# with open('style.css') as f:
#     st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# # col1, col2 = st.columns(2)
# # col1.metric("Column1")
# # col1.metric("Column2")

# components.html(
#     """
#     <head>
#     <link href="{% static 'fontawesomefree/css/fontawesome.css' %}" rel="stylesheet" type="text/css">
#     <link href="{% static 'fontawesomefree/css/brands.css' %}" rel="stylesheet" type="text/css">
#     <link href="{% static 'fontawesomefree/css/solid.css' %}" rel="stylesheet" type="text/css">
#     </head>
#     <i class="fa-solid fa-om"></i>
#     """,
# )
