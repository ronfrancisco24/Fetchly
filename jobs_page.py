import streamlit as st

css = """
    .st-key-main_container {
        background-color: rgb(250, 250, 250);
        padding: 1em;
        color: black;
        border-radius: 0.5rem;
        max-height: 40rem;
        overflow: auto;
    }
    
    [class*="st-key-job_listing_"] {
        background-color: rgb(250, 250, 250);
        padding: 1em;
        color: black;
        border-radius: 0.5rem;
        border: solid 1px #ccc; 
        border-left: solid #28c762;
        margin-bottom: 1rem;
    }
    
    [class*="secondary_container_"] {
        background-color: rgba(40, 199, 98, 0.2);
        border-radius: 0.5rem;
        padding: 1em;
        color: #145839;
    }
    
    .st-key-last_updated,
    .st-key-companies,
    .st-key-found_jobs {
        background-color: #15843f;
        border-radius: 0.5rem;
        padding: 1em;
        text-align:center;
        font-weight: bold;
    }
    
    """

def render_jobs():
    st.markdown("# Job Listings 💼")
    st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
    st.sidebar.button("Download", use_container_width=True, key="download_btn")
    
    st.sidebar.markdown("# Job Listings 💼")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')

    st.html(f"<style>{css}</style>")
    
    main_container = st.container(key='job_listing_main')

    with main_container:
        st.write('#### Get Started with Job Listings')
        
        st.write('Click the "Start Fetching" button in the sidebar to begin collecting the latest job opportunities')
        
        left_column, right_column = main_container.columns(2)
        
        with left_column.container(key='secondary_container_1', height='stretch'):
            st.write('##### What you will get: ')
            st.write(' - Job titles and descriptions')
            st.write(' - Company Information')
            st.write(' - Location Details')
            
        with right_column.container(key='secondary_container_2', height='stretch'):
            st.write('##### Job Types: ')
            st.write(' - Full-Time Positions')
            st.write(' - Contract Work')
            
def mark_column(column, css_key, number, description):
    with column.container(key=css_key):
        st.write(f'**{number}**')
        st.write(description)
            
def display_jobs():
    st.sidebar.markdown("# Job Listings 💼")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')

    st.html(f"<style>{css}</style>")
    
    top_container = st.container()
    
    column1, column2, column3 = top_container.columns(3)
   
    mark_column(column=column1, css_key='found_jobs', number='4', description='Jobs Found')
    mark_column(column=column2, css_key='companies', number='4', description='Jobs Found')
    mark_column(column=column3, css_key='last_updated', number='4', description='Jobs Found')
    
        
    main_container = st.container(key='main_container')
    
     
    main_container.write('### Job Listing Results')
    
    # Sample jobs
    jobs = [
        {"title": "Python Developer", "company": "Tech Corp", "location": 'San Francisco, CA', "posted": '1-24-25', "type": "Full Time"},
        {"title": "Data Scientist", "company": "AI Company", "location": 'Chicago, IL', "posted": '1-24-25', "type": "Full Time"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
        {"title": "Web Developer", "company": "StartupXYZ", "location": 'Los Angeles, CA', "posted": '1-26-25', "type": "Contract"},
    ]
    
    # Create containers with pattern-based keys
    for i, job in enumerate(jobs):
        job_container = main_container.container(key=f'job_listing_{i}')
        with job_container:
            st.write(f"**{job['title']}** at {job['company']}")
            col1, col2= job_container.columns(2)
            col1.write(f'**Location:** {job['location']}')
            col1.write(f'**Type:** {job['type']}')
            col2.write(f'**Posted:** {job['posted']}')
            col2.button('**↗ More Info Here!**',  key=f'more_info_{i}')
