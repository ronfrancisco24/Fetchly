import streamlit as st
import pandas as pd

# Main page content

st.sidebar.markdown("# Fetchly 🎈")
st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')

st.markdown("# Welcome to Fetchly 🎈")

st.write("""Fetchly is a modular, all-in-one web application that brings together the latest tech articles, trending movies, and remote job listings into a single dashboard. Built with Python, Streamlit, Plotly, and BeautifulSoup, Fetchly helps users explore data from multiple sources in a clean, interactive interface.

Unlike traditional scrapers that only dump raw text, Fetchly is designed to go a step further:

📰 Tech Articles → Stay up to date with the latest developments in the tech industry. View articles in a clean format, explore raw data, or analyze overall trends such as word frequencies and sentiment.

🎬 Trending Movies → See what’s popular in film today using external APIs. Explore movie posters, ratings, and analytics like genre breakdowns and average ratings.

💼 Remote Job Listings → Browse jobs scraped from reputable job boards (like WeWorkRemotely). Filter by contract type (Full-Time/Contract), analyze job type distribution, and view salary insights where available.

Fetchly also includes analytics and visualization features powered by Plotly, transforming raw scraped data into meaningful insights. Whether you’re exploring tech trends, planning your next movie night, or job-hunting, Fetchly centralizes it all in one intuitive app.""")

df = pd.DataFrame({
    'first column': ['Home 🎈', 'Jobs 💼', 'Articles 📰', 'Movies 🎬'],
    })

option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

st.sidebar.button('Start')

st.sidebar.button('Download')