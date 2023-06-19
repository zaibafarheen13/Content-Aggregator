from flask import render_template, request
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/w/api.php"

def get_wiki_content(url):
    try:
        req_obj = requests.get(url)
        text = req_obj.text
        soup = BeautifulSoup(text)
        all_paras = soup.find_all("p")
        wiki_text = ''.join(list(map(lambda p: p.text, all_paras)))
        return wiki_text
    except FileNotFoundError:
        return "Error retrieving Wikipedia content."

class Wiki:
    @staticmethod
    def wiki():
        wiki_url = '/wiki'
        weather_url = '/weather'
        news_url = '/news'
        home_url = '/'
        feed_url = '/feed'
        data = {}
        q = ''
        url_content = ''
        if request.method == "POST":
            url = request.form.get("url")
            url_content = get_wiki_content(url)
            for i in range(0, 200, 3):
                url_content = url_content.replace(f'[{i}]', '  ').replace(f'[{i+1}]', '  ').replace(f'[{i+2}]', '  ')

        if request.args.get("q"):
            try:
                response = requests.get(URL, params={
                    "action": "query",
                    "format": "json",
                    "list": "search",
                    "srsearch": request.args.get("q")
                })
                data = response.json()
                q = request.args.get("q")
            except NameError:
                data = {"error": "Error retrieving search results."}

        return render_template("wiki.html", data=data, q=q, url_content=url_content,  home_url=home_url, news_url=news_url, weather_url=weather_url, wiki_url=wiki_url, feed_url=feed_url)
