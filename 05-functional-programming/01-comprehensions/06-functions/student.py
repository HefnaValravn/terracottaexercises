def movie_count(movies, director):
    return len([movie.title for movie in movies if movie.director == director])


def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])


def has_director_made_genre(movies, director, genre):
    return any([movie.title for movie in movies if movie.director == director and genre in movie.genres])


def is_prime(n):
    return len([number for number in range(1, n+1) if n % number == 0]) == 2


def is_increasing(ns):
    return all(ns[i] <= ns[i + 1] for i in range(len(ns) - 1))


def count_matching(xs, ys):
    return len([item for item in xs if item in ys and xs.index(item) == ys.index(item)])


def weighted_sum(ns, weights):
    return sum(pair[0] * pair[1] for pair in zip(ns, weights))


def alternating_caps(string):
    return ''.join([letter.upper() if number % 2 == 0 else letter for number, letter in enumerate(string)])


def find_repeated_words(sentence):
    words = sentence.lower().split()
    words = [''.join(w for w in word if w.isalnum()) for word in words]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}