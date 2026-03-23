import pickle
import streamlit as st
import requests

# ---------------- CONFIG ----------------
API_KEY = "dee2577d49367dc11d35705ee6099a99"

st.set_page_config(page_title="Movie Recommender", layout="wide")

# ---------------- FETCH POSTER ----------------
@st.cache_data
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=dee2577d49367dc11d35705ee6099a99&language=en-US"
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            return "https://via.placeholder.com/500x750?text=No+Image"

        data = response.json()
        poster_path = data.get('poster_path')

        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"

    except Exception as e:
        print("Error:", e)
        return "https://via.placeholder.com/500x750?text=Error"


# ---------------- RECOMMEND FUNCTION ----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# ---------------- LOAD DATA ----------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity_small.pkl', 'rb'))

movie_list = movies['title'].values


# ---------------- UI ----------------
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Search or select a movie",
    movie_list
)

# ---------------- BUTTON ----------------
if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i], width=200)
            st.caption(names[i])


