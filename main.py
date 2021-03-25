from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

# Database
db = {
    
}

@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        exixtingJobs = db.get(word)
        # db에 검색한 job이 존재하면 기존의 job
        if  exixtingJobs:
            jobs = exixtingJobs
        # 없으면 Scrap    
        else:
            jobs = get_jobs(word)
            db[word] = jobs
        
    else: 
        return redirect("/")
    return render_template("report.html", 
    word=word, 
    
    resultsNumber=len(jobs),
    jobs=jobs
    )

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception() # Exception()이 실행되면 아래의 except 구분 실행
        print(word)
        word = word.lower()
        jobs = db.get(word)
        print(jobs)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")  
app.run(host="0.0.0.0")



