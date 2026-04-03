import re

def get_gemini_score(resume_text, jd_text):
    def extract_keywords(text):
        words = re.findall(r'\b[a-zA-Z][a-zA-Z+#.]{2,}\b', text.lower())
        stopwords = {'the','and','for','with','that','this','are','was','has','have',
                    'you','our','your','will','from','they','been','their','more',
                    'which','about','into','also','must','should','would','could',
                    'experience','knowledge','skills','ability','strong','good',
                    'work','working','build','building','using','use','based'}
        return set(w for w in words if w not in stopwords and len(w) > 2)

    jd_keywords = extract_keywords(jd_text)
    resume_keywords = extract_keywords(resume_text)
    common = jd_keywords & resume_keywords
    semantic_score = round(min(len(common) / max(len(jd_keywords), 1) * 150, 100), 1)

    resume_lower = resume_text.lower()
    exp_signals = ['intern','engineer','developer','scientist','analyst',
                   'built','developed','designed','deployed','managed']
    exp_count = sum(1 for s in exp_signals if s in resume_lower)
    exp_score = min(exp_count * 12, 100)

    tech_skills = {
        'python':'Python','sql':'SQL','machine learning':'Machine Learning',
        'nlp':'NLP','flask':'Flask','tensorflow':'TensorFlow',
        'deep learning':'Deep Learning','llm':'LLM','generative ai':'Generative AI',
        'pandas':'Pandas','numpy':'NumPy','git':'Git','docker':'Docker',
        'aws':'AWS','postgresql':'PostgreSQL','react':'React',
        'power bi':'Power BI','tableau':'Tableau','keras':'Keras',
        'scikit-learn':'Scikit-learn','xgboost':'XGBoost','gemini':'Gemini API'
    }

    jd_lower = jd_text.lower()
    resume_skills = [name for key, name in tech_skills.items() if key in resume_lower]
    jd_required = [name for key, name in tech_skills.items() if key in jd_lower]
    missing = [s for s in jd_required if s not in resume_skills]

    if semantic_score >= 75:
        summary = f"Strong candidate with {len(common)} keyword matches. Resume aligns well with the job requirements."
    elif semantic_score >= 50:
        summary = f"Good candidate with {len(common)} keyword matches. Some gaps exist but overall profile is relevant."
    else:
        summary = f"Partial match with {len(common)} keyword overlaps. Consider tailoring your resume to better match this role."

    strengths = []
    if 'python' in resume_lower: strengths.append("Strong Python programming background")
    if any(x in resume_lower for x in ['flask','api','rest']): strengths.append("Backend & API development experience")
    if any(x in resume_lower for x in ['gemini','llm','generative']): strengths.append("Hands-on GenAI & LLM experience")
    if any(x in resume_lower for x in ['machine learning','scikit','xgboost']): strengths.append("Solid ML model building skills")
    if any(x in resume_lower for x in ['deployed','deployment','production']): strengths.append("End-to-end deployment experience")
    if not strengths:
        strengths = ["Relevant technical background", "Project experience present"]

    improvements = []
    if missing: improvements.append(f"Add missing skills to resume: {', '.join(missing[:3])}")
    if 'aws' not in resume_lower and 'azure' not in resume_lower and 'gcp' not in resume_lower:
        improvements.append("Add cloud platform experience (AWS / GCP / Azure)")
    if 'docker' not in resume_lower:
        improvements.append("Learn Docker for containerization — highly in demand")
    if not improvements:
        improvements = ["Quantify achievements with numbers", "Add links to live projects on GitHub"]

    return {
        "semantic_score": semantic_score,
        "experience_match": exp_score,
        "summary": summary,
        "strengths": strengths[:3],
        "improvements": improvements[:3]
    }