import pickle
from flask import render_template, request
import requests
import json

API_KEY_NEWS = 'cea2661de68e46ef90da70903c65a905'

class News:
    @staticmethod
    def news():
        wiki_url = '/wiki'
        weather_url = '/weather'
        news_url = '/news'
        home_url = '/'
        feed_url = '/feed'
        if request.method == 'POST':
            source = request.form.get('search')
            url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'.format(source, API_KEY_NEWS)
            response = requests.get(url)
            data = json.loads(response.text)
            
            if 'articles' not in data:
                error_message = 'Unable to fetch news articles. Please try again later.'
                return render_template('news.html', error_message=error_message, home_url=home_url, news_url=news_url, weather_url=weather_url, wiki_url=wiki_url)
            
            articles = data['articles']
            
            # Add image URL to each article dictionary
            for article in articles:
                article['image'] = article.get('urlToImage')

            with open('news.dat', 'wb') as f:
                pickle.dump(data, f)

            return render_template('news.html', articles=articles, home_url=home_url, news_url=news_url, weather_url=weather_url, wiki_url=wiki_url,  feed_url=feed_url)
        else:
            return render_template('news.html', home_url=home_url, news_url=news_url, weather_url=weather_url, wiki_url=wiki_url,  feed_url=feed_url)
