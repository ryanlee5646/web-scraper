from indeed import extract_indeed_pages, extract_indeed_jobs


# 마지막 페이지를 가져오는 Function
last_indeed_pages = extract_indeed_pages()

# 모든 일자리를 반환하는 함수
indeed_jobs = extract_indeed_jobs(last_indeed_pages)


#### 모든 페이지에 job title 추출