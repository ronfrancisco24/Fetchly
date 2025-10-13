import streamlit as st
from styles import JOBS_CSS
from data_fetchers.jobs import fetch_job_listings
# sample jobs for testing.

jobs = fetch_job_listings()
    
def render_jobs():
    st.html(f"<style>{JOBS_CSS}</style>")
    st.markdown("# Job Listings 💼")
    st.sidebar.markdown("# Job Listings 💼")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    
    if 'jobs_fetched' not in st.session_state:
        st.session_state.jobs_fetched = False
        
    if st.session_state.jobs_fetched:
        display_jobs()
        clear = st.sidebar.button('Clear Results', use_container_width=True, key="clear_btn")
        if clear:
            st.session_state.jobs_fetched = False
            st.rerun()
    else:
        initial_content()
        fetch = st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
        if fetch:
            st.session_state.jobs_fetched = True
            st.rerun()  
        

def initial_content():
    main_container = st.container(key='job_listing_main')

    with main_container:
        st.write('#### Get Started with Job Listings')
        
        st.write('Click the "Start Fetching" button in the sidebar to begin collecting the latest job opportunities')
        
        left_column, right_column = main_container.columns(2)
        
        with left_column.container(key='accented_container_1', height='stretch'):
            st.write('##### What you will get: ')
            st.write(' - Job titles and descriptions')
            st.write(' - Company Information')
            st.write(' - Location Details')
            
        with right_column.container(key='accented_container_2', height='stretch'):
            st.write('##### Job Types: ')
            st.write(' - Full-Time Positions')
            st.write(' - Contract Work')
            
def mark_column(column, css_key, number, description):
    with column.container(key=css_key):
        st.write(f'**{number}**')
        st.write(description)
            
def display_jobs():
    st.sidebar.button("Download", use_container_width=True, key="download_btn")
    
    top_container = st.container()
    
    column1, column2, column3 = top_container.columns(3)
   
    mark_column(column=column1, css_key='stats_container_1', number='4', description='Jobs Found')
    mark_column(column=column2, css_key='stats_container_2', number='4', description='Jobs Found')
    mark_column(column=column3, css_key='stats_container_3', number='4', description='Jobs Found')
    
    main_container = st.container(key='main_container')
    filter_container = main_container.container(key='filter_container')
    
    filter_col1, filter_col2 = filter_container.columns(2)
    
    show_list = filter_col1.button('Listing', key='list', use_container_width=True)
    show_analytics = filter_col2.button('Articles', key='Analytics', use_container_width=True)
    
    main_container.write('### Job Listing Results')
    
    if show_analytics:
        display_analytics(main_container)
    else:
        display_article_results(main_container)
        
def display_article_results(main_container):
    for i, job in enumerate(jobs):
        job_container = main_container.container(key=f'job_listing_{i}')
        with job_container:
            st.write(f"**{job['title']}** at {job['company']}")
            col1, col2= job_container.columns([5,1])
            col1.write(f'**Location:** {job['location']}')
            # col1.write(f'**Type:** {job['type']}')
            col2.write(f"**Posted:** {job['posted']}")
            col2.markdown(f'<a href="{job['link']}" target="_blank"><button style="background-color:#4CAF50; color:white; border:none; border-radius:4px; padding:8px 16px; cursor:pointer;">**↗ More Info**</button></a>', unsafe_allow_html=True)
            
def stats_labels(number, label):
    st.markdown(f'<div class="stats-number">{number}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="stats-label">{label}</div>', unsafe_allow_html=True)
    
def progress_bar_stats(label, percentage):
    st.markdown(f'{label} — {round(percentage * 100)}%')
    st.progress(percentage)
    
def display_analytics(main_container):
    col1, col2 = main_container.columns(2)
    with col1.container(key='secondary_container_type', height='stretch'):
        st.markdown('###### Jobs By Type')
        total_jobs = len(jobs)
        jobs_count = {}
        
    with col2.container(key='secondary_container_stats', height='stretch'):
        st.write('###### Summary Stats')
        stats_labels(4, 'Total Jobs')
        stats_labels(5, 'Total Unique Companies')
    
    