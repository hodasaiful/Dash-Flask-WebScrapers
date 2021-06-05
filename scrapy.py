from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as soup

my_url = "https://www.imdb.com/search/title/?release_date=1950-01-01,2012-12-31&sort=num_votes,desc"
uClient = UReq(my_url)  
page_html = uClient.read()
uClient.close()

filename = ("D:\scrapy.csv")
f = open(filename, "w")
headers = "Name, Years, Runtime \n"
f.write(headers)

page_soup = soup(page_html, "html.parser")
Containers = page_soup.findAll("div", {"class":"lister-item mode-advanced"})

print(Containers)

for container in Containers:
    name = container.img["alt"]
    year_mov = container.findAll("span", {"class":"lister-item-year"})
    year = year_mov[0].text
    runtime_mov = container.findAll("span", {"class":"runtime"})
    runtime = runtime_mov[0].text
    f.write(name + "," + year + "," + runtime + "\n")

f.close()

import pandas as pd
imdb = pd.read_csv("D:\scrapy.csv")
print(imdb.head())






