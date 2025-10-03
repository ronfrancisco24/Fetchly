import streamlit as st
import pandas as pd
from home_page import render_home
from jobs_page import render_jobs
from movies_page import render_movies
from articles_page import render_articles
import base64 

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("images/background-image.png")
        
page_options = ["Home", "Jobs", "Articles", "Movies"]
    
selected_page = st.sidebar.selectbox(
    "Fetch Options",
    page_options
)

st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
st.sidebar.button("Download", use_container_width=True, key="download_btn")

st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    
    [data-testid="stSidebarContent"] {{
        background: rgb(40, 112, 124)
    }}
    
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0)
    }}
    
    [data-testid="stIconMaterial"] {{
        color: rgba(250,250,250, 1)
    }}
    
    </style>
    """, unsafe_allow_html=True)
    
def handle_page(page):
    match page:
        case "Home":
            render_home()
        case "Jobs":
            render_jobs()
        case "Articles":
            render_articles()
        case "Movies":
            render_movies()
        case _:
            render_home()
            
handle_page(selected_page)
