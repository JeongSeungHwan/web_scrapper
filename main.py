from indeed import *
from save import save_to_csv as save
from flask import Flask, render_template, request, redirect, send_file

app = Flask("SuperScrapper")

#fake db
db = {}


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get("word")
    if word:
        word = word.upper()
        if db.get(word) :
            jobs = db.get(word)
        else :    
            jobs = search_job(word)
            db[word] = jobs
        jobs_len = len(jobs)
        return render_template("report.html", searching = word, length = jobs_len, jobs = jobs)
        
    else :
        return redirect("/")

@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word :
            raise Exception()
        word = word.upper()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save(jobs, word)
        return send_file(f"{word}.csv") #파일저장
    except :
        return redirect("/")

app.run(host="192.168.137.1")