
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def terribleMethod():

    print("Welcome to our diagnostics tools \n")
    error = (input("What is the issue you are facing? \n")).lower()
    print("\n")

    websiteSynonyms = ["website","webpage","page","site","youtube","wikipedia","twitter","instagram","amazon","pinterest","imdb","es","facebook","fandom","apple","ja","de","live","cricbuzz","fr","linkedin","globo","microsoft","nytimes","etsy","it","mayoclinic","healthline","indiatimes","amazon","amazon","bbc","ikea","amazon","amazon","indeed","flipkart","bbc","espn","mail","ebay","hurriyet","allegro","booking","mercadolivre","britannica","google","kompas","nih","cnn","merriam-webster","homedepot","amazpn","ar","detik","nike","medlineplus","id","brainly","milliyet","accuweather","magazineluiza","marca","medicalnewstoday","cdc","hepsiburada","cambridge","cookpad","m","dailymail","as","ilovepdf","gsmarena","byjus","amazon","adobe","investing","epfindia","clevelandclinic","aliexpress","espncricinfo","india","ndtv","canva","amazon","craigslist","finance","dailymotion","indiamart","kinopoisk","nl","onet","omegle","goal","americanas","investopedia","dictionary","mail","ebay","naver","hm","hotstar","bestbuy","collinsdictionary"]


    x=0
    while x < len(websiteSynonyms):
        if websiteSynonyms[x] in error and "load" in error:
            q1 = (input("Are you connected to the wifi\n")).lower()
            if q1 == "yes":
                q2a = (input("Have you tried multiple websites\n")).lower()
                if q2a == "yes":
                    q3a = (input("Does your network icon show any issues (E.G No Internet Connection)\n")).lower()
                    if q3a == "yes":
                        print("Restart your device's wifi connection\n")
                        q4a = input("Did that work?\n")
                if q2a == "no":
                    print("Try multiple websites\n")
            if q1 == "no":
                q2b = (input("Do you use ethernet (A cable connects your computer to the router\n)")).lower()
                if q2b == "yes":
                    print("Check whether the cable is plugged in and if so try a different cable\n")
                if q2b == "no":
                    print("Connect to your wifi\n")
            break
        else:
            x+=1

#terribleMethod

def betterMethodHopefully ():

    print("Possible Errors\n\n")
    print("1. Wi-Fi won't connect \n")
    print("2. Can't download an app \n")

    choice = int(input("Enter a number "))

#betterMethodHopefully()

def bestMethod():

   headersUnfil = []
   descriptionsUnfil = []
   headers = []
   hrefs = []
   descriptions = []

   text=input("Enter Problem: ")
   url = "https://support.microsoft.com/en-GB/search/results?query="+ text + "&isEnrichedQuery=false"

   req = requests.get(url)
   soup = BeautifulSoup(req.text, features="lxml")
   html = (req.text)
   html = html.split(">")

   for i in range(len(html)):
    if 'class="header"' in html[i]:
        headersUnfil.append(html[i])
        print(html[i])
    if 'class="description"' in html[i]:
        descriptionsUnfil.append(html[i])
        #print(html[i])

    for i in range(len(headersUnfil)):
        temp = headersUnfil[i]
        temp.split("class")

    print(headersUnfil)
bestMethod()