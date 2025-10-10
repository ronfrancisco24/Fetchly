from data_fetchers.jobs import fetch_job_listings
from data_fetchers.articles import fetch_technology_articles
from data_fetchers.movies import fetch_popular_movies

def main():
    jobs = fetch_job_listings()
    articles = fetch_technology_articles()
    movies = fetch_popular_movies()
    print(movies[0])
    
if __name__ == "__main__":
    main()

#TODO: have a global css instead. 



    


