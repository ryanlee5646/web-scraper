from indeed import get_jobs as get_indeed_jobs
from so import get_jobs as get_so_jobs
from save import save_to_file
from flask import Flask

app = Flask("SuperScrapper")

@app.route('/')
def home():
    return 'Hello! Welcome!'

@app.route("/contact")
def potato():
    return "Contact me!"

app.run(host="0.0.0.0")


# # stackoverflow jobs
# so_jobs = get_so_jobs()

# # indeed_jobs
# indeed_jobs = get_indeed_jobs()

# jobs = so_jobs + indeed_jobs
# # jobs = indeed_jobs

# # CSV(Comma Seperated Values) 파일 만들기
# save_to_file(jobs)
