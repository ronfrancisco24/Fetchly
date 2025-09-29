from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import requests
import time
import json

# # TMDB API

# # Access Top 20 Popular Movies from TMDB API
movie_auth_url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

movie_header = {
    "accept": "application/json",
    "Authorization": BEARER_TOKEN 
}

def fetch_popular_movies():
# # Fetch Response
    movies_response = requests.get(movie_auth_url, headers=movie_header)

    movies = movies_response.text

    # Parse the JSON response
    movies_data = json.loads(movies)

    # Access the list of movies (usually under 'results')
    movies_top_20 = movies_data.get('results', [])

    movies_list = []

    for movie in movies_top_20:
        title = movie['title']
        overview = movie['overview']
        release_date = movie['release_date']
        language = movie['original_language']
        
        movies_list.append({
            'title': title,
            'overview': overview,
            'release_date': release_date,
            'language': language 
        })
        
    return movies_list


    
    