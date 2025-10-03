import streamlit as st

css = """
    .st-key-my_blue_container {
        background-color: rgb(250, 250, 250);
        padding: 1em;
        color: black;
        border-radius: 0.5rem;
        border-left: solid #3b82f6;
    }
    
    .st-key-my_left_container, 
    .st-key-my_right_container {
        background-color: rgba(59, 130, 246, 0.2);
        border-radius: 0.5rem;
        padding: 1em;
        color: #1e3a8a;
    }
    """
    
def render_articles():
    st.markdown("# Tech News Page 🔬")
    st.sidebar.markdown("# Articles Page 🔬")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
    st.sidebar.button("Download", use_container_width=True, key="download_btn")

    st.html(f"<style>{css}</style>")
    
    main_container = st.container(key='my_blue_container')

    with main_container:
        st.write('#### Get Started with Job Listings')
        
        st.write('Click the "Start Fetching" button in the sidebar to begin collecting the technology news from top sources.')
        
        left_column, right_column = main_container.columns(2)
        
        with left_column.container(key='my_left_container', height='stretch'):
            st.write('##### What you will get: ')
            st.write(' - Latest Headlines')
            st.write(' - Article Summaries')
            st.write(' - Publication Dates')
            st.write(' - Direct links to articles')
            
        with right_column.container(key='my_right_container', height='stretch'):
            st.write('##### Job Types: ')
            st.write(' - TechCrunch')
            st.write(' - Wired')
            st.write(' - More Coming Soon...')
    