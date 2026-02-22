import streamlit as st
import pickle
import requests
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Netflix Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# 🔐 Your TMDB API Key
API_KEY = "5510d83e3f4c94f7af317f84534590c6"

# ---------------- NETFLIX STYLE CSS ----------------
st.markdown("""
<style>

/* Background */
.stApp {
    background-color: #141414;
}

/* Remove extra padding */
.block-container {
    padding-top: 2rem;
}

/* Netflix Title */
.netflix-title {
    font-size: 50px;
    font-weight: bold;
    color: #E50914;
    text-align: center;
    margin-bottom: 5px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #b3b3b3;
    font-size: 18px;
    margin-bottom: 40px;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #333333 !important;
    color: white !important;
    border-radius: 8px;
}

/* Button */
.stButton>button {
    background-color: #E50914;
    color: white;
    font-weight: bold;
    border-radius: 6px;
    padding: 10px 30px;
    border: none;
}

.stButton>button:hover {
    background-color: #f40612;
    transform: scale(1.05);
    transition: 0.2s;
}

/* Movie Card */
.movie-card {
    transition: transform 0.3s ease;
}

.movie-card:hover {
    transform: scale(1.08);
}

.movie-title {
    color: white;
    font-size: 16px;
    font-weight: 500;
    text-align: center;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
movies = pickle.load(open("model.pkl", "rb"))
similarity = joblib.load("similarity_compressed.pkl.z")

# ---------------- FETCH POSTER ----------------
import time

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    for _ in range(3):  # Retry 3 times
        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                poster_path = data.get("poster_path")

                if poster_path:
                    return f"https://image.tmdb.org/t/p/w500{poster_path}"

            time.sleep(0.5)  # small delay before retry

        except requests.exceptions.RequestException:
            time.sleep(0.5)

    return "https://via.placeholder.com/300x450?text=No+Poster"

# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    movie_index = movies[movies['movie_name'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].movie_name)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ---------------- UI ----------------

# Header
st.markdown('<div class="netflix-title">NETFLIX MOVIE RECOMMENDER</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Discover movies similar to your favorites</div>', unsafe_allow_html=True)

# Movie Selection
selected_movie = st.selectbox(
    "Choose a Movie",
    movies['movie_name'].values
)

# Recommendation Button
if st.button("Get Recommendations 🎬"):
    with st.spinner("Finding best matches for you..."):
        names, posters = recommend(selected_movie)

    st.markdown("### 🔥 Recommended For You")

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):
        with col:
            st.markdown('<div class="movie-card">', unsafe_allow_html=True)
            st.image(poster)
            st.markdown(f'<div class="movie-title">{name}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<center style='color:gray'>Built with ❤️ using Streamlit</center>",
    unsafe_allow_html=True

)

