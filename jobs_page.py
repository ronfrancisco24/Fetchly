import streamlit as st


def render_jobs():
    st.markdown("# Job Listings 💼")
    
    st.sidebar.markdown("# Job Listings 💼")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')

    css = """
    .st-key-my_blue_container {
        background-color: rgb(250, 250, 250);
        padding: 1em;
        color: black;
        border-radius: 0.5rem;
        border-left: solid #28c762;
    }
    
    .st-key-my_left_container {
        background-color: rgba(40, 199, 98, 0.2);
        border-radius: 0.5rem;
        padding: 1em;
        color: #145839;
    }
    
    .st-key-my_right_container {
        background-color: rgba(40, 199, 98, 0.2);
        border-radius: 0.5rem;
        padding: 1em;
        color: #145839;
    }
    """

    st.html(f"<style>{css}</style>")
    
    main_container = st.container(key='my_blue_container')

    with main_container:
        st.write('#### Get Started with Job Listings')
        
        st.write('Click the "Start Fetching" button in the sidebar to begin collecting the latest job opportunities')
        
        left_column, right_column = main_container.columns(2)
        
        with left_column.container(key='my_left_container'):
            st.write('##### What you will get: ')
            st.write(' - Job titles and descriptions')
            st.write(' - Company Information')
            st.write(' - Location Details')
            
        with right_column.container(key='my_right_container'):
            st.write('##### Job Types: ')
            st.write(' - Full-Time Positions')
            st.write(' - Contract Work')