from flask import render_template, request

class Index():
    
    @staticmethod
    def index():
        wiki_url = '/wiki'
        weather_url = '/weather'
        news_url = '/news'
        home_url = '/'
        feed_url = '/feed'
        return render_template('index.html', home_url=home_url, news_url=news_url, weather_url=weather_url, wiki_url=wiki_url,  feed_url=feed_url)
