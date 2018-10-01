import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)

    for post_text in soup.findAll('a', {'class':'home-nav__link home-nav__link--client'}):
        content = post_text.string
        words = content.lower().split()
        print(words)


start("https://oldschool.runescape.com/a=12/")