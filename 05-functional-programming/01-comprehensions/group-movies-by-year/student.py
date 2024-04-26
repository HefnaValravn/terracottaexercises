def group_movies_by_year(movies):
    answer = {}
    for year in {movie.year for movie in movies}:
        answer[year] = [movie.title for movie in movies if movie.year == year]

    return answer