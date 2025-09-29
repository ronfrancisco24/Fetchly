from bs4 import BeautifulSoup
import requests
import time

technology_articles_url = "https://news.ycombinator.com/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

    
# Technology Scraper

def fetch_technology_articles():
    article_response = requests.get(technology_articles_url, headers=header)
    article_text = article_response.text

    article_soup = BeautifulSoup(article_text, 'html.parser')
    articles = article_soup.find_all(name='span', class_='titleline')
    article_score = article_soup.find_all(name='span', class_='score')

    article_data = []

    for article, score in zip(articles, article_score):
        anchor = article.find(name='a')
        if anchor:
            title = anchor.getText()
            link = anchor.get('href')
            score_text = score.getText()
            
        article_data.append({
            'title': title,
            'link': link,
            'score': score_text
        })
        
    return article_data