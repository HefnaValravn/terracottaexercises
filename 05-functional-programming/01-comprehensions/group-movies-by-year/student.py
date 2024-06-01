def group_movies_by_year(movies):
    return {movie.year: [movie2.title for movie2 in movies if movie2.year == movie.year] for movie in movies}