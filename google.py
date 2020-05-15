from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import time
import smtplib , ssl
from login import sender_email, receiver_email, password
run = 0
def email(website):

    message = "Check this out this is the link:" + website
    port = 465
    context = ssl._create_default_https_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message)

def checkExists(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

while True: 
    run += 1
    print(run)
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    with open("websiteList.csv") as f:
        reader = csv.reader(f)
        siteList = list(reader)
        #print(siteList)
        for i in siteList:
            driver.get(i[0])
            time.sleep(4)
            xPath = i[1]
            exists = checkExists(xPath)
            if exists == True: 
                text = driver.find_element_by_xpath(xPath).text
                if text != i[2]:
                    print("negative")
                else:
                    print("POSITIVE RIGHT HERE")
                    email(i[0])
            else:
                print("POSITIVE RIGHT HERE")
                email(i[0])
    time.sleep(8*60)
    


