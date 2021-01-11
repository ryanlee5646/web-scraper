import requests
from bs4 import BeautifulSoup

indeed_url= requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_url.text, 'html.parser')

pagination = indeed_soup.find("div", {"class":"pagination"})

# 모든 <a>태그 찾기
links = pagination.find_all('a')

pages = []
for link in links[:-1]: # 마지막 태그는 삭제
    # pages.append(link.find("span").string) # <span>태그에서 string만 가져오기
    pages.append(int(link.string)) # 링크 전체에서 string만 가져오기
    
max_page = pages[-1] # 마지막 페이지 번호

#### 다음 강의는 페이지당 limit 개수 부터