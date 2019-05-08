import re
import requests
from flask import Flask
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

HOST = '0.0.0.0'
PATTERN_URL = 'https://habr.com/'
PATTERN_WORD = r'\b[\w]{6}\b'


def replace_words(html):
    for word in html.find_all(text=re.compile(PATTERN_WORD)):
        word.replace_with(re.sub(PATTERN_WORD, lambda w: w.group(0)+'™', word))
    return html


def replace_hrefs(html):
    for a in html.find_all('a', 'href' is not None):
        host = 'http://{}:5000/'.format(HOST)
        a['href'] = a['href'].replace(PATTERN_URL, host)
    return html


@app.route('/')
@app.route('/<path:path>')
def index(path=''):
    r = requests.get(PATTERN_URL + path)
    res = bs(r.text, 'lxml')
    res = replace_hrefs(res)
    res = replace_words(res)
    return res.prettify('utf-8')


if __name__ == '__main__':
    app.run(host=HOST)
