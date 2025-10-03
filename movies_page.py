import streamlit as st

css = """
    .st-key-my_blue_container {
        background-color: rgb(250, 250, 250);
        padding: 1em;
        color: black;
        border-radius: 0.5rem;
        border-left: solid #6d21ac;
    }
    
    .st-key-my_left_container,
    .st-key-my_right_container {
        background-color: rgba(109, 33, 172, 0.1);
        border-radius: 0.5rem;
        padding: 1em;
        color: #581c87;
    }
    """

def render_movies():
    st.markdown("# Movies 🎬")
    st.sidebar.markdown("# Movies 🎬")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
    st.sidebar.button("Download", use_container_width=True, key="download_btn")

    st.html(f"<style>{css}</style>")
    
    main_container = st.container(key='my_blue_container')

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
            
def display_movies():
    main_container = st.container(key='my_blue_container')
    