#https://www.w3schools.com/
import requests 
from bs4 import BeautifulSoup
import html5lib

url="https://www.w3schools.com/"
req=requests.get(url)
print(req.content)
bp=BeautifulSoup(req.content, 'html5lib')
print(bp.prettify())


tal=bp.findAll('div',{'class':'w3-col l3 m6'})
for i in tal:
    
    for title in i.findAll('h3'):
        #cnt=title.find('h3')
        #lst=cnt("alt").split("#")
        print(title.text)



