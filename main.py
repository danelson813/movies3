# movies3/main.py
import pandas as pd
from helpers.utils import get_soup

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
base = 'https://imdb.com'
soup = get_soup(url,'data/html.txt', True)

movies = soup.find_all('div', class_='ipc-metadata-list-summary-item__c')

results = []
for movie in movies:
    title = movie.find('h3').text
    rank = title.split(' ', 1)[0]
    title = title.split(' ', 1)[1]
    items = movie.find('div',class_='sc-300a8231-6 dBUjvq cli-title-metadata').find_all("span")
    year = items[0].text
    run_time =  items[1].text
    rating = items[2].text
    movie_link = base + movie.find('h3').find_parent('a').get('href')
    result = {
        'rank': rank,
        'title': title,
        'year': year,
        'run_time': run_time,
        'rating': rating,
        'movie_link': movie_link
    }
    results.append((result))
df = pd.DataFrame(results)
df.to_csv("data/results.csv", index=False)
