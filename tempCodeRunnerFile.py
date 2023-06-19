from flask import Flask
from news import News
from speech import Speech
from weather import Weather
from index import Index
from feed import Feed
from wiki import Wiki

app = Flask(__name__)

@app.route('/')
def index():
    return Index.index()

@app.route('/news/', methods=['GET', 'POST'])
def news():
    return News.news()

@app.route('/feed/', methods=['GET', 'POST'])
def feed():
    return Feed.feed()

@app.route('/weather/', methods=['GET', 'POST'])
def weather():
    return Weather.weather()

@app.route('/speech/<text>')
def speech(text):
    return Speech.speak(text)

@app.route("/wiki/", methods=["GET", "POST"])
def wiki():
    return Wiki.wiki()

if __name__ == '__main__':
    app.run(debug=True)
