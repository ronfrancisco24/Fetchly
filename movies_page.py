import streamlit as st
from styles import MOVIES_CSS

def render_movies():
    st.markdown("# Movies 🎬")
    st.sidebar.markdown("# Movies 🎬")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
    st.sidebar.button("Download", use_container_width=True, key="download_btn")

    st.html(f"<style>{MOVIES_CSS}</style>")
    
    main_container = st.container(key='movie_listing_main')

    with main_container:
        st.write('#### Get Started with Popular Movies')
        
        st.write('###### Click the "Start Fetching" button in the sidebar to discover the latest trending movies.')
        
        left_column, right_column = main_container.columns(2)
        
        with left_column.container(key='my_left_container', height='stretch'):
            st.write('##### What you will get: ')
            st.write(' - Movie Titles')
            st.write(' - Genre Information')
            st.write(' - Director Details')
            
        with right_column.container(key='my_right_container', height='stretch'):
            st.write('##### Categories: ')
            st.write(' - Action and Adventure')
            st.write(' - Drama and Romance')
            st.write(' - Sci-Fi and Fantasy')
            st.write(' - Comedy and More')
            
def mark_column(column, css_key, number, description):
    with column.container(key=css_key):
        st.write(f'**{number}**')
        st.write(description)
            
def display_movies():
    st.sidebar.markdown("# Job Listings 💼")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
    
    st.html(f"<style>{MOVIES_CSS}</style>")
    
    top_container = st.container()
    
    column1, column2, column3 = top_container.columns(3)
   
    mark_column(column=column1, css_key='stats_container_1', number='4', description='Movies Found')
    mark_column(column=column2, css_key='stats_container_2', number='4', description='Movies Found')
    mark_column(column=column3, css_key='stats_container_3', number='4', description='Movies Found')
    
        
    main_container = st.container(key='main_container')
    
    main_container.write('### Movies Results')
    
    # sample jobs for testing.
    jobs = [
        {"title": "Python Developer", "company": "Tech Corp", "location": 'San Francisco, CA', "posted": '1-24-25', "type": "Full Time"},
        {"title": "Data Scientist", "company": "AI Company", "location": 'Chicago, IL', "posted": '1-24-25', "type": "Full Time"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
    ]
    
    for i, job in enumerate(jobs):
        job_container = main_container.container(key=f'movie_listing_{i}')
        with job_container:
            st.write(f"**{job['title']}** at {job['company']}")
            col1, col2= job_container.columns([5,1])
            col1.write(f'**Location:** {job['location']}')
            col1.write(f'**Type:** {job['type']}')
            col2.write(f'**Posted:** {job['posted']}')
            col2.button('**↗ More Info Here!**', key=f'more_info_{i}')

    