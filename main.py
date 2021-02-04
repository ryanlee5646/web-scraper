from flask import Flask, render_template, request, redirect
from scrapper import get_jobs

app = Flask("SuperScrapper")

# Fake Database
db = {}

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
        # if fromDb:
            # jobs = fromDb
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


app.run(host="0.0.0.0")
