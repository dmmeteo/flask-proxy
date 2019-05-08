import re
import requests
from flask import Flask
from bs4 import BeautifulSoup as bs

app = Flask(__name__)


@app.route('/')
@app.route('/<path:path>')
def index(path=''):
    r = requests.get('habr.com/' + path)
    return res.prettify('utf-8')


if __name__ == '__main__':
    app.run()
