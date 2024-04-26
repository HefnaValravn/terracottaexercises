def title_to_director(movies):
    return {movie.title:movie.director for movie in movies}


def director_to_titles(movies):
    directors = {movie.director: [] for movie in movies}

    for movie in movies:
        directors[movie.director].append(movie.title)
    
    return directors
                
