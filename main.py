
from bs4 import BeautifulSoup
import requests


a = "california"
print(a.lower().replace(" ", "-"))

html_text = requests.get("https://wildfiretoday.com/tag/"+a+"/" , timeout = (3.05 , 20) ).text
# print(html_text)

soup = BeautifulSoup(html_text , 'html.parser' )
print(soup)
news_article_blob = soup.find('div' , id='primary'  )
# print(news_article_blob)

news_article = news_article_blob.find_all('article')


for news_piece in news_article:
    news_title = news_piece.h2.text
    news_link = news_piece.a['href']
    # news_location_blob = news_piece.find('div' , class_='meta-section')
    # news_location = news_location_blob.find('span' , class_='tags-links').a.text
    print(news_title)
    print('\n')
    print(news_link)





