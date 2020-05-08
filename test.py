from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import time
import smtplib , ssl
from login import sender_email, receiver_email, password
import requests
from lxml import html, etree


def email(website):

    message = "Check this out this is the link:" + website
    port = 465
    context = ssl._create_default_https_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message)

while True: 

    with open("websiteList.csv") as f:
        
        reader = csv.reader(f)
        siteList = list(reader)
        #print(siteList)
        for i in siteList:
            page = requests.get(i[0])
            time.sleep(4)
            xPath = i[1]
            extractedHtml = html.fromstring(page.content)
            text = extractedHtml.xpath(xPath)[0].text
            if text != i[2]:
                print("negative")
            else:
                email(i[0])
    time.sleep(60*60)