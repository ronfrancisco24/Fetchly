import streamlit as st

def render_home():
    st.sidebar.markdown("# Fetchly")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')

    st.markdown("# Welcome to Fetchly!")

    st.write("""Fetchly is a modular, all-in-one web application that brings together the latest tech articles, trending movies, and remote job listings into a single dashboard. Built with Python, Streamlit, Plotly, and BeautifulSoup, Fetchly helps users explore data from multiple sources in a clean, interactive interface.
    Unlike traditional scrapers that only dump raw text, Fetchly is designed to go a step further:
    Fetchly also includes analytics and visualization features powered by Plotly, transforming raw scraped data into meaningful insights. Whether you’re exploring tech trends, planning your next movie night, or job-hunting, Fetchly centralizes it all in one intuitive app.""")

    st.write("#### Choose a fetcher from the sidebar to get started! ")
    
    left_column, middle_column, right_column = st.columns(3)


    container_messages = ['<h5>📰 Tech Articles</h4> <br>Stay up to date with the latest developments in the tech industry. View articles in a clean format, explore raw data, or analyze overall trends such as word frequencies and sentiment.',
                        '<h5>🎬 Trending Movies</h4> <br>See what’s popular in film today using external APIs. Explore movie posters, ratings, and analytics like genre breakdowns and average ratings.',
                        '<h5>💼 Job Listings</h4> <br>Browse jobs scraped from reputable job boards (like WeWorkRemotely). Filter by contract type (Full-Time/Contract), analyze job type distribution, and view salary insights where available.']
        
    def mark_column(column, message, color):
        with column:
            st.markdown(f"""
            <div style="border-left: solid {color}; color:#000000; background-color: #fff; padding-left: 1em; padding: 1em; border-radius: 0.5em; margin-bottom: 4px; height:30rem; font-size: 1rem;">
            {message}
            </div>
        """, unsafe_allow_html=True)
            
    mark_column(left_column, container_messages[0], "#194bd6")
    mark_column(middle_column, container_messages[1], '#28a745')
    mark_column(right_column, container_messages[2], '#6f42c1')