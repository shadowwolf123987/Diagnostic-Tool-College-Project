
import requests
from bs4 import BeautifulSoup

def bestMethod():

   headersUnfil = []
   descriptionsUnfil = []
   headers = []
   hrefs = []
   descriptions = []
   count=0

   print("\n")
   text=input("Enter Problem: ")
   url = "https://support.microsoft.com/en-GB/search/results?query="+ text + "&isEnrichedQuery=false"

   req = requests.get(url)
   soup = BeautifulSoup(req.text, features="lxml")
   html = (req.text)
   html = html.replace("<b>","")
   html = html.replace("</b>","")
   html = html.split(">")

   for i in html:
    count+=1 #I know I should use enumerate but its too tedious
    if 'class="header"' in i:
        headersUnfil.append(i)
    if 'class="description"' in i:
        html[count] = (html[count].replace("</div","")).strip()
        descriptions.append(html[count])

   x=0
   while x < len(headersUnfil):
        temp = headersUnfil[x]
        temp = temp.split('"')
        hrefs.append(temp[3])
        headers.append(temp[5])
        x+=1

   x=0
   while x < len(headers):
       print("\n")
       print("Title: "+headers[x])
       print("\n")
       print("Description:\n"+descriptions[x])
       print("\n")
       print("URL:\n"+hrefs[x])
       print("\n"*2)
       x+=1

bestMethod()