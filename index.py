from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import requests
import csv
import etree

driver = webdriver.Chrome(executable_path='chromedriver.exe')
with open("websiteList.csv") as f:
    reader = csv.reader(f)
    siteList = list(reader)
    url = siteList[1][0]
    driver.get(url)
    res = requests.get(url)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.get_text()
    whiteList = [
        "PRE-RELEASE",
        "AUTO NOTIFY",
        "Auto-Notify",
    ]
    for i in whiteList:
        print(text.find(i))
    

  


