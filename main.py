from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


options = webdriver.Chrome()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(
    "/usr/local/bin/chromedriver", options=options)


driver.get(
    "https://www.cricbuzz.com/cricket-series/3961/icc-mens-t20-world-cup-2022/matches")

# series-matches > div:nth-child(7)
# page-wrapper > div.cb-bg-white.cb-col-100.cb-col.cb-hm-rght.cb-series-filters
classes = "cb-bg-white.cb-col-100.cb-col.cb-hm-rght.cb-series-filters"
classes_split = classes.replace(".", " ")

print(classes)


content = driver.page_source
soup = BeautifulSoup(content)
page_wrapper = soup.find("div", attrs={"class": classes})


scores = []
stories = []
fixtures = []
