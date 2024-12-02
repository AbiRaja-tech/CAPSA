import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Bombay_Stock_Exchange"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("Page Title:", soup.title.string)
paragraphs = soup.find_all('p')
for para in paragraphs:
    if para.get_text(strip=True):
        print("First Paragraph:", para.get_text(strip=True))
        break
