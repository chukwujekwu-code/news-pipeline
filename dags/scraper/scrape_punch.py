import requests
from bs4 import BeautifulSoup

def get_headlines():
    url = "https://punchng.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    headlines = []
    for h2 in soup.find_all("h2"):
        text = h2.get_text(strip=True)
        if text:
            headlines.append(text)
    return headlines


print(get_headlines())