from bs4 import BeautifulSoup
import requests

url = "www.bromcomvle.com/Homework/"
page = requests.get("https://" + url)
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
