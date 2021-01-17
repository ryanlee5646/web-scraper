import requests
from bs4 import BeautifulSoup

LIMIT = 50 
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

# Indeed 페이지에서 마지막 페이지 번호 가져오는 메서드
def get_last_page():
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

# Indeed 페이지에서 직업의 상세정보를 가져오는 메서드
def extract_job(html):
    title = html.find("h2", {"class": "title"}).find("a")["title"]
    company = html.find("span", {"class":"company"})
    
    # 회사명 가져오기
    if company:
        company_anchor = company.find("a")
        
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
        company = company.strip()
    else:
        company = None
    
    # 장소 가져오기
    location = html.find("div", {"class": "recJobLoc"})["data-rc-loc"]

    # 직업id (link에 담을 변수)
    job_id = html['data-jk']

    return {
        'title': title, 
        'company':company, 
        'location':location, 
        'link':f'https://www.indeed.com/viewjob?jk={job_id}'
    }

def extract_jobs(last_pages):
    jobs = []
    for page in range(last_pages):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page * LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
    # 회사명 찾기
    results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
    
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs

def get_jobs():
    # 마지막 페이지를 가져오는 Function
    last_page = get_last_page()
    # 모든 일자리를 반환하는 함수
    jobs = extract_jobs(last_page)
    return jobs