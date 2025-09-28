import streamlit as st
import numpy as np
import pandas as pd

# Define the pages
main_page = st.Page("main_page.py", title="Welcome to Fetchly", icon="🎈")
page_2 = st.Page("jobs.py", title="Job", icon="💼")
page_3 = st.Page("movies.py", title="Movies", icon="🎬")
page_4 = st.Page("articles.py", title="Articles", icon="📰")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3, page_4])

# Run the selected page
pg.run()