import requests
from bs4 import BeautifulSoup


LIMIT = 50 
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

# Indeed 페이지에서 마지막 페이지 번호 가져오는 메서드
def extract_indeed_pages():
    url= requests.get(URL)
    soup = BeautifulSoup(url.text, 'html.parser')
    pagination = soup.find("div", {"class":"pagination"})

    # 모든 <a>태그 찾기
    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]: # 마지막 태그는 삭제
        # pages.append(link.find("span").string) # <span>태그에서 string만 가져오기
        pages.append(int(link.string)) # 링크 전체에서 string만 가져오기        
    
    max_page = pages[-1] # 마지막 페이지 번호
    return max_page 


def extract_indeed_jobs(last_pages):
    for page in range(last_pages):
        jobs = []
        result = requests.get(f"{URL}&start={page * LIMIT}")
        
    return jobs

