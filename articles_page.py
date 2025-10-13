import streamlit as st
from styles import ARTICLES_CSS
    
# sample articles for testing.
articles = [
    {"title": "AI Breakthrough in Machine Learning", "source": "TechCrunch", "category": "AI", "published": "1-24-25", "read_time": "5 min"},
    {"title": "New Framework for Web Development", "source": "Wired", "category": "Web Dev", "published": "1-24-25", "read_time": "3 min"},
    {"title": "Quantum Computing Advances", "source": "TechCrunch", "category": "Hardware", "published": "1-26-25", "read_time": "7 min"},
    {"title": "Cybersecurity Trends 2025", "source": "Ars Technica", "category": "Security", "published": "1-26-25", "read_time": "6 min"},
    {"title": "Cloud Infrastructure Updates", "source": "Wired", "category": "Cloud", "published": "1-26-25", "read_time": "4 min"},
    {"title": "Mobile App Development Tools", "source": "TechCrunch", "category": "Mobile", "published": "1-26-25", "read_time": "5 min"},
    {"title": "Data Science Best Practices", "source": "MIT Tech Review", "category": "Data", "published": "1-26-25", "read_time": "8 min"},
]
    
def render_articles():
    st.html(f"<style>{ARTICLES_CSS}</style>")
    st.markdown("# Tech News Page 🔬")
    st.sidebar.markdown("# Articles Page 🔬")
    st.sidebar.markdown('Your all-in-one hub for **Tech News, Trending Movies, and Remote Jobs** — powered by Python, Streamlit, and BeautifulSoup.')
    
    # Initialize session state
    if 'articles_fetched' not in st.session_state:
        st.session_state.articles_fetched = False
    
    if st.session_state.articles_fetched:
        display_articles()
        clear = st.sidebar.button('Clear Results', use_container_width=True, key="clear_btn")
        if clear:
            st.session_state.articles_fetched = False
            st.rerun() 
    else:
        initial_content()
        fetch = st.sidebar.button("Fetch Data!", use_container_width=True, key="fetch_btn")
        if fetch:
            st.session_state.articles_fetched = True
      
    
def initial_content():
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
    st.sidebar.button("Download", use_container_width=True, key="download_btn")
    
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
    
    main_container.write('### Tech News Results')

    if show_analytics:
        display_analytics(main_container)
    else:
        display_article_results(main_container)
        
def display_article_results(main_container):
    for i, article in enumerate(articles):
        article_container = main_container.container(key=f'article_listing_{i}')
        with article_container:
            st.write(f"##### {article['title']} at *{article['source']}*")
            col1, col2= article_container.columns([5,1])
            col1.write(f'**Category:** {article['category']}')
            col1.write(f'**Read Time:** {article['read_time']}')
            col2.write(f'**Published:** {article['published']}')
            col2.button('**↗ More Info Here!**',  key=f'more_info_{i}')
            
    
def progress_bar_stats(label, percentage):
    st.markdown(f'{label} — {round(percentage * 100)}%')
    st.progress(percentage)
    
def stats_labels(number, label):
    st.markdown(f'<div class="stats-number">{number}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="stats-label">{label}</div>', unsafe_allow_html=True)
    
def display_analytics(main_container):
    col1, col2 = main_container.columns(2)
    with col1.container(key='secondary_container_type', height='stretch'):
        
        st.markdown('###### Sources')
        total_articles = len(articles)
        source_count = {}
        for article in articles:
            source = article['source']
            if source in source_count:
                source_count[source] += 1
            else:
                source_count[source] = 1
                
        for source, count in source_count.items():
            percentage = count / total_articles
            progress_bar_stats(source, percentage)
    
    with col2.container(key='secondary_container_stats', height='stretch'):
        st.write('###### Summary Stats')
        stats_labels(4, 'Total Jobs')
        stats_labels(5, 'Total Unique Companies')
    
    