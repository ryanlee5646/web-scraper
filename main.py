import requests
from bs4 import BeautifulSoup

indeed_url= requests.get("https://www.indeed.com/jobs?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=20&sort=&psf=advsrch&from=advancedsearch")

indeed_soup = BeautifulSoup(indeed_url.text, 'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})

# 모든 <a>태그 찾기
pages = pagination.find_all('a')

# 모든 <span> 태그 찾기 
spans = []
for page in pages:
    spans.append(page.find("span"))
    print(page.find("span"))
# 마지막 <span> 태그는 삭제
spans = spans[:-1]
