from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import requests
import time
import json


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

job_listings_url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
technology_articles_url = "https://news.ycombinator.com/"

# Job Scraper

# job_response = requests.get(job_listings_url, headers=header)
# job_text = job_response.text

# job_soup = BeautifulSoup(job_text, 'html.parser')
# job_lists = job_soup.find_all(name='li', class_="new-listing-container")

# jobs = []

# # Scrape Job Listings.

# for job in job_lists:
#     # Exclude ad listings.
#     if 'feature--ad' in job.get('class', []):
#         continue
    
#     title = job.find(name='h3', class_='new-listing__header__title')
#     company = job.find(name='p', class_='new-listing__company-name')
#     location = job.find(name='p', class_='new-listing__company-headquarters')
#     date_posted = job.find(name='p', class_='new-listing__header__icons__date')
#     link = job.find_all(name='a')
    
#     # If there are more than one anchor tags select the 2nd one. (This is because the main link for the application is the 2nd link.)
#     if len(link) > 1:
#         web_link = link[1].get('href')
        
#     jobs.append(
#         {
#             'title': title.getText(),
#             'company': company.getText(),
#             'location': location.getText(),
#             'date_posted': date_posted.getText(),
#             'link': f'weworkremotely.com{web_link}'
#         }
#     )    
    
# print(jobs[1])
    
# Technology Scraper

# article_response = requests.get(technology_articles_url, headers=header)
# article_text = article_response.text

# article_soup = BeautifulSoup(article_text, 'html.parser')
# articles = article_soup.find_all(name='span', class_='titleline')
# article_score = article_soup.find_all(name='span', class_='score')

# article_data = []

# for article, score in zip(articles, article_score):
#     anchor = article.find(name='a')
#     if anchor:
#         title = anchor.getText()
#         link = anchor.get('href')
#         score_text = score.getText()
        
#     article_data.append({
#         'title': title,
#         'link': link,
#         'score': score_text
#     })
    
# print(article_data[0])

# # TMDB API

# # Access Top 20 Popular Movies from TMDB API
# movie_auth_url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"

# load_dotenv()
# BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# movie_header = {
#     "accept": "application/json",
#     "Authorization": BEARER_TOKEN 
# }

# # Fetch Response
# movies_response = requests.get(movie_auth_url, headers=movie_header)

# movies = movies_response.text

# # Parse the JSON response
# movies_data = json.loads(movies)

# # Access the list of movies (usually under 'results')
# movies_top_20 = movies_data.get('results', [])

# movies_list = []

# for movie in movies_top_20:
#     title = movie['title']
#     overview = movie['overview']
#     release_date = movie['release_date']
#     language = movie['original_language']
    
#     movies_list.append({
#         'title': title,
#         'overview': overview,
#         'release_date': release_date,
#         'language': language 
#     })
    
# print(movies_list[1])

    
    


    


