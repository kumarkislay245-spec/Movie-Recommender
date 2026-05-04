<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:141414,50:E50914,100:141414&height=200&section=header&text=Movie%20Recommender&fontSize=48&fontColor=ffffff&fontAlignY=38&desc=Netflix-Style%20Content-Based%20Recommendation%20Engine&descAlignY=60&descColor=b3b3b3" width="100%"/>

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![TMDB API](https://img.shields.io/badge/TMDB-01B4E4?style=for-the-badge&logo=themoviedatabase&logoColor=white)
![Pickle](https://img.shields.io/badge/Pickle%20%2B%20Joblib-grey?style=for-the-badge)

[![GitHub Repo](https://img.shields.io/badge/View%20Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/kumarkislay245-spec/Movie-Recommender)
[![Author](https://img.shields.io/badge/Author-Kislay%20Kumar-50c88c?style=for-the-badge)](https://github.com/kumarkislay245-spec)

</div>

---

## 🎬 What Is This?

A **Netflix-inspired movie recommendation web app** that suggests 5 similar Bollywood movies based on whatever film you search for — complete with live movie posters fetched in real-time from the TMDB API.

Unlike collaborative filtering (which needs user history), this system works using **pure content-based filtering** — it understands *what a movie is* (genre, cast, plot) and finds others that are most similar. No login needed, no cold-start problem.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎨 **Netflix-style UI** | Dark `#141414` background, red accents, hover animations — built entirely with custom CSS in Streamlit |
| 🖼️ **Live Movie Posters** | Fetches real poster images from the **TMDB API** for every recommendation |
| ⚡ **Smart Caching** | `@st.cache_data` ensures poster fetches are cached — same movie never hits the API twice |
| 🔁 **Retry Logic** | API calls auto-retry up to 3 times with a delay — handles network failures gracefully |
| 💾 **Compressed Model** | Similarity matrix stored as `.pkl.z` (zlib-compressed) — reduces file size for faster loading |
| 🎯 **Top-5 Recommendations** | Returns the 5 most similar movies ranked by cosine similarity score |

---

## 🧠 How It Works

```
User selects a movie
        │
        ▼
Look up movie index in the dataset (model.pkl)
        │
        ▼
Load pre-computed similarity matrix (similarity_compressed.pkl.z)
        │
        ▼
Sort all movies by cosine similarity score → pick top 5
        │
        ▼
Fetch each movie's poster from TMDB API (with retry + cache)
        │
        ▼
Display Netflix-style recommendation cards
```

### The ML Pipeline (what happens in the notebook)

1. **Data Loading** — Load Bollywood movie dataset with movie names, IDs, and metadata
2. **Feature Extraction** — Extract meaningful features: genres, cast, plot keywords
3. **Vectorization** — Convert text features into numerical vectors using `CountVectorizer` / `TF-IDF`
4. **Cosine Similarity** — Compute pairwise similarity scores across the entire movie catalog
5. **Model Saving** — Serialize the movies dataframe as `model.pkl` and the similarity matrix as `similarity_compressed.pkl.z`

---

## 📁 Project Structure

```
Movie-Recommender/
│
├── Untitled0.ipynb          # ML pipeline: data processing, vectorization, similarity computation
├── file1.py                 # Streamlit web app (Netflix UI + TMDB API integration)
├── model.pkl                # Serialized movies dataframe (movie names + IDs)
├── similarity_compressed.pkl.z  # Zlib-compressed cosine similarity matrix
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/kumarkislay245-spec/Movie-Recommender.git
cd Movie-Recommender
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the app
```bash
streamlit run file1.py
```

### 4. Open in browser
```
http://localhost:8501
```

> **Note:** The app uses the TMDB API to fetch movie posters. An API key is already configured in `file1.py`. If you fork this project, get your own free key at [themoviedb.org](https://www.themoviedb.org/settings/api).

---

## 📦 Dependencies

```txt
streamlit
scikit-learn
pandas
numpy
requests
joblib
pickle
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 🖼️ App Preview

> *The app opens with a Netflix-dark interface. Select any Bollywood movie from the dropdown, click "Get Recommendations 🎬", and instantly see 5 similar movies with their posters displayed in a responsive 5-column grid.*

---

## 🔑 Key Technical Decisions

**Why content-based filtering over collaborative?**
Collaborative filtering needs user rating history. This dataset has no user data — content-based filtering works from day one with zero cold-start issues.

**Why compress the similarity matrix?**
The cosine similarity matrix for a large movie catalog is an N×N float matrix — it gets large fast. Using `joblib` with zlib compression (`similarity_compressed.pkl.z`) keeps the file small without sacrificing lookup speed.

**Why retry logic on the API?**
TMDB's free tier occasionally drops requests under load. The 3-attempt retry with `time.sleep(0.5)` between attempts ensures the UI never breaks just because one poster failed to load.

---

## 👨‍💻 Author

**Kislay Kumar** — NIT Warangal

[![GitHub](https://img.shields.io/badge/GitHub-kumarkislay245--spec-181717?style=flat-square&logo=github)](https://github.com/kumarkislay245-spec)

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:141414,50:E50914,100:141414&height=100&section=footer" width="100%"/>
</div>
