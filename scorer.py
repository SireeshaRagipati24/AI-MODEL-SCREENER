import math
import re
from collections import Counter

def get_tfidf_score(resume_text, jd_text):
    def get_tokens(text):
        return re.findall(r'\w+', text.lower())

    res_words = get_tokens(resume_text)
    jd_words = get_tokens(jd_text)

    if not jd_words or not res_words:
        return 0

    res_cnt = Counter(res_words)
    jd_cnt = Counter(jd_words)
    common_words = set(res_cnt.keys()) & set(jd_cnt.keys())
    dot_product = sum(res_cnt[w] * jd_cnt[w] for w in common_words)
    mag_res = math.sqrt(sum(v**2 for v in res_cnt.values()))
    mag_jd = math.sqrt(sum(v**2 for v in jd_cnt.values()))

    if mag_res * mag_jd == 0:
        return 0

    return round((dot_product / (mag_res * mag_jd)) * 100, 2)

def get_skill_gap(resume_text, jd_text):
    skills_list = [
        "python", "sql", "machine learning", "nlp", "flask", "tensorflow",
        "keras", "scikit-learn", "pandas", "numpy", "git", "docker",
        "aws", "react", "postgresql", "mysql", "deep learning", "llm",
        "generative ai", "gemini", "power bi", "tableau", "xgboost"
    ]
    res_lower = resume_text.lower()
    jd_lower = jd_text.lower()
    required = [s for s in skills_list if s in jd_lower]
    matched = [s for s in required if s in res_lower]
    missing = [s for s in required if s not in res_lower]
    return matched, missing