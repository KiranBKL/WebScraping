import requests
from bs4 import BeautifulSoup as bs
result=requests.get("https://www.whitehouse.gov/briefing-room/")
print(result.status_code)
src=result.content
soup=bs(src,'lxml')
urls=[]
h2_tag=soup.find_all("h2")
for i in h2_tag:
    a_tag=i.find('a')
    try:
        if 'href' in a_tag.attrs:
            urls.append(a_tag.attrs['href'])
    except:
        pass
#print(urls)
for i in urls:
    print(i,"\n")
