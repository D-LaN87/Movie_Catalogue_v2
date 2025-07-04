import requests

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNjA0MDMwZGM4ZGQzYmIxYWU0ZmY0NWRhMTY4ZmQ5NCIsIm5iZiI6MTc1MTYyMDgwMy41ODgsInN1YiI6IjY4Njc5Y2MzNDI1ODhjNDQzMzdhYjhlNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.QGm9tSLlUVDFigyQ2MGtarkNUEPyyecTG1Z1ccpWL-I"
API_BASE_URL = "https://api.themoviedb.org/3"
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_popular_movies():
    endpoint = f"{API_BASE_URL}/movie/popular"
    response = requests.get(endpoint, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type="popular"):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"{API_BASE_URL}/movie/{movie_id}"
    response = requests.get(endpoint, headers=HEADERS, params={"language": "pl-PL"})
    response.raise_for_status()
    return response.json()

def get_movie_cast(movie_id):
    endpoint = f"{API_BASE_URL}/movie/{movie_id}/credits"
    response = requests.get(endpoint, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('cast', [])

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()