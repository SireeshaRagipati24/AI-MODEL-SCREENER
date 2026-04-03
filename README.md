# 🤖 AI Resume Screener & Interview Coach

An intelligent, high-precision ATS tool that analyzes resumes against Job Descriptions using **Hybrid NLP (Cosine Similarity)** and **Semantic AI (Gemini)**. It provides deep analysis, skill gap detection, and dynamic interview preparation.

---

## ✨ Features
- 📄 **PDF Extraction** — High-accuracy text parsing using PyMuPDF.
- 🧠 **Hybrid Scoring** — Combines **TF-IDF Vectorization** with **LLM Semantic Analysis**.
- 🚀 **Dynamic Interview Prep** — Automatically generates 3 tough technical questions based on resume gaps.
- 🎯 **Perfect Fit Guide** — Specific advice on exactly what keywords or phrases to add to reach a 100% match.
- 📊 **Visual Analytics** — Animated match bars, A/B/C/D grading, and strength highlights.
- 🎨 **Modern Dark UI** — Premium purple-gradient aesthetic with glassmorphism effects.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend** | Python, Flask |
| **AI Model** | Google Gemini 1.5 Flash |
| **NLP Logic** | Cosine Similarity, Scikit-learn (Custom), Counter |
| **PDF Parsing** | PyMuPDF (fitz) |
| **Frontend** | HTML5, CSS3 (Modern Gradients), JavaScript (Async/Fetch) |
| **Deployment** | Render / Gunicorn |

---

## 📁 Project Structure

```text
ai-resume-screener/
├── templates/
│   └── index.html        # Modern Responsive Frontend
├── app.py                # Flask API & Route Handling
├── parser.py             # PDF Text Extraction Engine
├── scorer.py             # Mathematical Keyword Matching Logic
├── gemini_scorer.py      # AI Semantic Analysis & Question Generator
├── requirements.txt      # Project Dependencies
└── .env                  # Environment Variables (API Keys)

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-screener.git
cd ai-resume-screener
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python app.py
```

**4. Open browser**

---

## 📸 How It Works

1. Upload your resume (PDF format)
2. Paste the job description
3. Click **Analyze Resume**
4. Get instant results:
   - Overall grade (A/B/C/D)
   - Keyword match score
   - Semantic match score
   - Skill-by-skill breakdown
   - Strengths & areas to improve

## 👩‍💻 Built By

**Sireesha Ragipati** — Associate Data Scientist  
[LinkedIn](https://linkedin.com) • [GitHub](https://github.com/YOUR_USERNAME)
