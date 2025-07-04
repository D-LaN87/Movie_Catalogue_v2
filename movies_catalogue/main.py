from flask import Flask, render_template, request
import tmdb_client
import random

app = Flask(__name__)

MOVIE_LISTS = {
    "popular": "Popularne",
    "top_rated": "Najlepiej oceniane",
    "upcoming": "Nadchodzące"
}

@app.route('/')
def homepage():
    list_type = request.args.get('list_type', 'popular')

    #Validation
    if list_type not in MOVIE_LISTS.keys():
        list_type = "popular"  # if incorrect we go to 'popular' section

    movies = tmdb_client.get_movies(how_many=8, list_type=list_type)
    random.shuffle(movies)
    return render_template("homepage.html", movies=movies, current_list=list_type, movie_lists=MOVIE_LISTS)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    movie = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_movie_cast(movie_id)
    return render_template(
        "movie_details.html",
        movie=movie,
        cast=cast,
        movie_lists=MOVIE_LISTS,
        current_list="popular"
    )

if __name__ == '__main__':
    app.run(debug=True)
