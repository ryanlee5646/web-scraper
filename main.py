from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs

# stackoverflow jobs
so_jobs = get_so_jobs
# indeed_jobs
indeed_jobs = get_indeed_jobs()

jobs = so_jobs + indeed_jobs

print(jobs)

# CSV(Comma Seperated Values) 파일 만들기

