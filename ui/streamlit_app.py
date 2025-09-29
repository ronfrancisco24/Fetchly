import streamlit as st
import numpy as np
import pandas as pd

# Define the pages
main_page = st.Page("main_page.py", title="Welcome to Fetchly", icon="🎈")
jobs_page = st.Page("jobs_page.py", title="Job", icon="💼")
movies_page = st.Page("movies_page.py", title="Movies", icon="🎬")
article_page = st.Page("articles_page.py", title="Articles", icon="📰")

# Set up navigation
pg = st.navigation([main_page, jobs_page, movies_page, article_page])

option = st.sidebar.selectbox(
    'Which number do you like best?',
     ['Home 🎈', 'Jobs 💼', 'Articles 📰', 'Movies 🎬'])

#TODO: 
# if option in ['']:
#     st.navigate()

st.sidebar.button('Fetch Data!', width='stretch')

st.sidebar.button('Download', width='stretch')

# Run the selected page
pg.run()