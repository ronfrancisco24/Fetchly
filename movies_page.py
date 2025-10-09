import streamlit as st
from styles import MOVIES_CSS

# sample jobs for testing.
movies = [
    {"title": "Avatar: The Way of Water", "genre": "Sci-Fi", "director": "James Cameron", "rating": "8.2", "year": "2022"},
    {"title": "Top Gun: Maverick", "genre": "Action", "director": "Joseph Kosinski", "rating": "8.3", "year": "2022"},
    {"title": "Black Panther: Wakanda Forever", "genre": "Action", "director": "Ryan Coogler", "rating": "6.7", "year": "2022"},
    {"title": "Dune", "genre": "Sci-Fi", "director": "Denis Villeneuve", "rating": "8.0", "year": "2021"},
    {"title": "Spider-Man: No Way Home", "genre": "Action", "director": "Jon Watts", "rating": "8.4", "year": "2021"},
]

def render_movies():
    st.html(f"<style>{MOVIES_CSS}</style>")
    st.markdown("# Movies 🎬")
    st.sidebar.markdown("# Movies 🎬")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
    st.sidebar.button("Download", use_container_width=True, key="download_btn")

   
    main_container = st.container(key='movie_listing_main')

    with main_container:
        st.write('#### Get Started with Popular Movies')
        
        st.write('###### Click the "Start Fetching" button in the sidebar to discover the latest trending movies.')
        
        left_column, right_column = main_container.columns(2)
        
        with left_column.container(key='accented_container_1', height='stretch'):
            st.write('##### What you will get: ')
            st.write(' - Movie Titles')
            st.write(' - Genre Information')
            st.write(' - Director Details')
            
        with right_column.container(key='accented_container_2', height='stretch'):
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
    st.html(f"<style>{MOVIES_CSS}</style>")
    st.sidebar.markdown("# Job Listings 💼")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
    
    top_container = st.container()
    
    column1, column2, column3 = top_container.columns(3)
   
    mark_column(column=column1, css_key='stats_container_1', number='4', description='Movies Found')
    mark_column(column=column2, css_key='stats_container_2', number='4', description='Movies Found')
    mark_column(column=column3, css_key='stats_container_3', number='4', description='Movies Found')
    
    main_container = st.container(key='main_container')
    filter_container = main_container.container(key='filter_container')
    
    filter_col1, filter_col2 = filter_container.columns(2)
    
    main_container.write('### Movies Results')
    
    show_list = filter_col1.button('Movies', key='list', use_container_width=True)
    show_analytics = filter_col2.button('Analytics', key='Analytics', use_container_width=True)
    
    if show_analytics:
        display_analytics(main_container)
    else:
        display_movie_results(main_container)
    
def display_movie_results(main_container):
    for i, movie in enumerate(movies):
        movie_container = main_container.container(key=f'movie_listing_{i}')
        with movie_container:
            st.write(f"**{movie['title']}** at {movie['year']}")
            col1, col2= movie_container.columns([5,1])
            col1.write(f'**Genre:** {movie['genre']}')
            col1.write(f'**Director:** {movie['director']}')
            col2.write(f'**Rating:** {movie['rating']}/10')
            col2.button('**↗ More Info Here!**',  key=f'more_info_{i}')
            
def stats_labels(number, label):
    st.markdown(f'<div class="stats-number">{number}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="stats-label">{label}</div>', unsafe_allow_html=True)
    
def display_analytics(main_container):
    col1, col2 = main_container.columns(2)
    with col1.container(key='secondary_container_type', height='stretch'):
        # turn into articles by source
        st.markdown('###### Jobs By Type')
        st.markdown('Full - Time — 85%')
        st.progress(0.25)
        st.markdown('Contract — 25%')
        st.progress(0.55)
    
    with col2.container(key='secondary_container_stats', height='stretch'):
        st.write('###### Summary Stats')
        stats_labels(4, 'Total Jobs')
        stats_labels(5, 'Total Unique Companies')
    


    