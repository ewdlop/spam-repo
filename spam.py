import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for heading in soup.find_all('h2'):
        print(heading.text)

url = "https://example.com"
scrape_website(url)
