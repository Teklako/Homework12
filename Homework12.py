# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# r = requests.get(url)
# print(r.status_code)
# content = r.text
# soup = BeautifulSoup(content, 'html.parser')
# body = soup.find("body")
# wrapper = body.find("div", id='wrapper')
# redesign = wrapper.find('div', {'class': 'redesign'})
# page_content = redesign.find('div', id="pagecontent")
# pg_content = page_content.find_all('div', {'class': 'pagecontent'})[2]
# cont2 = pg_content.find('div', id="content-2-wide")
# main = cont2.find('div', id="main")
# article = main.find('div',{'class':'article'})
# ab_widget = article.find('span',{'class':'ab_widget'})
# seen_coll = ab_widget.find('div',{'class':'seen-collection'})
# article2 = seen_coll.find('div',{'class':'article'})
# lister = article2.find('div', {'class':'lister'})
# table = lister.find('table')
# tbody = lister.find('tbody')
# all_films = tbody.find_all('tr')
# for i in all_films:
#       title_col = i.find('td',{'class':'titleColumn'})
#       rating_col = i.find('td', {'class': 'ratingColumn imdbRating'})
#       text = title_col.a.text
#       rating = rating_col.strong.text
#       print(text, rating)
# print(all_films)

import requests
from bs4 import BeautifulSoup
import csv
import time
import datetime
url = "https://www.imdb.com/chart/top"
pause = 5
pages = 2
csv_file = open('top_rated_movies.csv', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title', 'Year'])
for i in range(pages):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    movie_list = soup.find('tbody', {'class': 'lister-list'}).find_all('tr')
    for movie in movie_list:
        title = movie.find('td', {'class': 'titleColumn'}).find('a').text
        year = movie.find('td', {'class': 'titleColumn'}).find('span').text.strip('()')
        csv_writer.writerow([title, year])
    time.sleep(pause)
    url = url + str(i+2)
csv_file.close()





