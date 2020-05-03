from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import time
import smtplib , ssl
from login import sender_email, receiver_email, password

driver = webdriver.Chrome(executable_path='chromedriver.exe')
with open("websiteList.csv") as f:
    reader = csv.reader(f)
    siteList = list(reader)
    #print(siteList)
    for i in siteList:
        driver.get(i[0])
        time.sleep(4)
        xPath = i[1]
        text = driver.find_element_by_xpath(xPath).text
        if text != i[2]:
            print("negative")
        else:
            email(i[0])



def email(website):

    message = "Check this out this is the link:" + website
    port = 465
    context = ssl._create_default_https_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message)