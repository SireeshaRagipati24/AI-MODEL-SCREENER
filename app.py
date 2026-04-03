from flask import Flask, request, jsonify, render_template
from parser import extract_resume_text
from scorer import get_tfidf_score, get_skill_gap
from gemini_scorer import get_gemini_score
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/screen", methods=["POST"])
def screen_resume():
    try:
        resume_file = request.files.get("resume")
        jd_text = request.form.get("job_description")
        if not resume_file or not jd_text:
            return jsonify({"error": "Missing inputs"}), 400

        file_path = os.path.join(UPLOAD_FOLDER, resume_file.filename)
        resume_file.save(file_path)

        resume_text = extract_resume_text(file_path)
        tfidf = get_tfidf_score(resume_text, jd_text)
        matched, missing = get_skill_gap(resume_text, jd_text)
        gemini = get_gemini_score(resume_text, jd_text)

        return jsonify({
            "tfidf_match_score": tfidf,
            "matched_skills": matched,
            "missing_skills": missing,
            "gemini_semantic_score": gemini["semantic_score"],
            "experience_match": gemini["experience_match"],
            "summary": gemini["summary"],
            "strengths": gemini["strengths"],
            "improvements": gemini["improvements"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)