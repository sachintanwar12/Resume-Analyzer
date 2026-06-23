from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SKILLS = ["python","java","html","css","javascript","mysql","php","react","nodejs"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form.get("resume_text","").lower()
    found = [s for s in SKILLS if s in text]
    job_skills = {"python","html","css","javascript","mysql","react"}
    score = int((len(set(found)&job_skills)/len(job_skills))*100)
    missing = list(job_skills - set(found))
    return render_template("result.html", skills=found, score=score, missing=missing)

if __name__ == "__main__":
    app.run(debug=True)
