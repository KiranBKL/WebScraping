import requests
from bs4 import BeautifulSoup as bs
result=requests.get("https://google.com/")
print(result.status_code)
#print(result.headers)
src=result.content
print("\n")
#print(src)
soup=bs(src,'lxml')
links=soup.find_all("a")
#print(links)
for link in links:
    if "About" in link.text:
        print(link)
        print("\n")
        print(link.attrs['href'])