import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

data = []

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    data.append([text,author])

df = pd.DataFrame(data, columns=["Quote", "Author"])

df.to_csv("quotes.csv", index=False)

print("Dataset Saved Successfully")