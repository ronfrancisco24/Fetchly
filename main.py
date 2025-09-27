from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import requests
import time


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

job_listings_url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
technology_url = "https://news.ycombinator.com/"
movies_url = "https://api.themoviedb.org/3/trending/movie/week"

job_response = requests.get(job_listings_url, headers=header)
job_text = job_response.text

job_soup = BeautifulSoup(job_text, 'html.parser')
job_lists = job_soup.find_all(name='li', class_="new-listing-container")

jobs = []

# Scrape Job Listings.

for job in job_lists:
    # Exclude ad listings.
    if 'feature--ad' in job.get('class', []):
        continue
    
    title = job.find(name='h3', class_='new-listing__header__title')
    company = job.find(name='p', class_='new-listing__company-name')
    location = job.find(name='p', class_='new-listing__company-headquarters')
    date_posted = job.find(name='p', class_='new-listing__header__icons__date')
    link = job.find(name='a')
        
    jobs.append(
        {
            'title': title.getText(),
            'company': company.getText(),
            'location': location.getText(),
            'date_posted': date_posted.getText(),
            'link': 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings'
        }
    )    
    
    

    
