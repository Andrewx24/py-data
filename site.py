from bs4 import BeautifulSoup
import requests


url="https://productivitysumo.com/"


def get_site(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup

print(get_site(url))