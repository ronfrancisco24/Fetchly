import streamlit as st
from styles import ARTICLES_CSS
    
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
    
def render_articles():
    st.html(f"<style>{ARTICLES_CSS}</style>")
    st.markdown("# Tech News Page 🔬")
    st.sidebar.markdown("# Articles Page 🔬")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    fetch = st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
    if fetch:
        display_articles()
        
    main_container = st.container(key='article_listing_main')

    with main_container:
        st.write('#### Get Started with Job Listings')
        st.write('Click the "Start Fetching" button in the sidebar to begin collecting the technology news from top sources.')
        
        left_column, right_column = main_container.columns(2)
        
        with left_column.container(key='accented_container_1', height='stretch'):
            st.write('##### What you will get: ')
            st.write(' - Latest Headlines')
            st.write(' - Article Summaries')
            st.write(' - Publication Dates')
            st.write(' - Direct links to articles')
            
        with right_column.container(key='accented_container_2', height='stretch'):
            st.write('##### Job Types: ')
            st.write(' - TechCrunch')
            st.write(' - Wired')
            st.write(' - More Coming Soon...')
            
def mark_column(column, css_key, number, description):
    with column.container(key=css_key):
        st.write(f'**{number}**')
        st.write(description)

def display_articles():
    st.sidebar.markdown("# Articles Page 🔬")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    st.sidebar.button('Clear', use_container_width=True, key="clear")
    st.sidebar.button("Download", use_container_width=True, key="download_btn")
    st.html(f"<style>{ARTICLES_CSS}</style>")
    
    top_container = st.container()
    
    column1, column2, column3 = top_container.columns(3)
   
    mark_column(column=column1, css_key='stats_container_1', number='4', description='Articles Found')
    mark_column(column=column2, css_key='stats_container_2', number='4', description='Articles Found')
    mark_column(column=column3, css_key='stats_container_3', number='4', description='Articles Found')
    
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
        job_container = main_container.container(key=f'article_listing_{i}')
        with job_container:
            st.write(f"**{job['title']}** at {job['company']}")
            col1, col2= job_container.columns([5,1])
            col1.write(f'**Location:** {job['location']}')
            col1.write(f'**Type:** {job['type']}')
            col2.write(f'**Posted:** {job['posted']}')
            col2.button('**↗ More Info Here!**',  key=f'more_info_{i}')
    
def display_analytics(main_container):
    col1, col2 = main_container.columns(2)
    with col1.container(key='secondary_container_type', height='stretch'):
        st.markdown('###### Jobs By Type')
        st.markdown('Full - Time — 85%')
        st.progress(0.25)
        st.markdown('Contract — 25%')
        st.progress(0.55)
    
    with col2.container(key='secondary_container_stats', height='stretch'):
        st.write('###### Summary Stats')
        st.markdown('<div class="stats-number">4</div>', unsafe_allow_html=True)
        st.markdown('<div class="stats-label">Total Jobs</div>', unsafe_allow_html=True)
        st.markdown('<div class="stats-number"">4</div>', unsafe_allow_html=True)
        st.markdown('<div class="stats-label">Total Unique Companies</div>', unsafe_allow_html=True)
    
    