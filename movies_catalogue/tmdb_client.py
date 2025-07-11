import requests
import os

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")
API_BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/"

def call_tmdb_api(endpoint):
    full_url = f"{API_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")

def get_movies(how_many, list_type="popular"):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}?language=pl-PL")

def get_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits").get("cast", [])

def get_poster_url(poster_api_path, size="w342"):
    return f"{IMAGE_BASE_URL}{size}/{poster_api_path}"