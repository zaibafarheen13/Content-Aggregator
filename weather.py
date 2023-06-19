from flask import render_template, request
import requests

API_KEY_WEATHER = '2d9d4f129fe49648d748c90d9df8bf3e'

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY_WEATHER}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None
    
class Weather:
    @staticmethod
    def weather():
        wiki_url = '/wiki'
        weather_url = '/weather'
        news_url = '/news'
        home_url = '/'
        feed_url = '/feed'
        weather = None
        if request.method == 'POST':
            city = request.form['city']
            weather = get_weather(city)
        return render_template('weather.html', weather=weather,  home_url=home_url, news_url=news_url, weather_url=weather_url, wiki_url=wiki_url, feed_url=feed_url)