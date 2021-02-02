import requests
from bs4 import BeautifulSoup

LIMIT = 50
# stackoverflow


# 마지막 페이지 가져오기
def get_last_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

# stackoverflow 직업 상세정보 가져오기
def extract_job(html):
    title = html.find("h2",{"class", "mb4"}).find("a")["title"]
     
    # 원래 find_all을 사용하게 되면 <span>태그의 하위 level의 <span>태그까지 전부 가져오게된다. 
    # recursive 속성을 사용하면 같은 level의 태그만 가져온다❗️ 
    company, location = html.find("h3",{"class", "fc-black-700"}).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-").strip("\n").strip("\r") #stirp으로 해당 공백 제거
    # 링크를 가져오기위한 job_id
    job_id = html["data-jobid"]
    return {
        'title':title,
        'company':company,
        'location':location,
        'link':f'https://stackoverflow.com/jobs/{job_id}/'
    }


def extract_jobs(last_page, URL):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping Stackoverflow: Page: {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        # 페이지마다 스크랩
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)            
    return jobs

def get_jobs(word):
    URL = f'https://stackoverflow.com/jobs?q={word}&sort=i'
    last_page = get_last_page(URL)
    jobs = extract_jobs(last_page, URL)
    
    return jobs
