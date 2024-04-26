import re

def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director])


def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])


def has_director_made_genre(movies, director, genre):
    return any([movie for movie in movies if movie.director == director and genre in movie.genres])


def is_prime(n):
    return len([number for number in range(1, n) if n % number == 0]) == 1


def is_increasing(ns):
    return ns == sorted(ns)


def count_matching(xs, ys):
    return len([pair for pair in zip(xs, ys) if pair[0] == pair[1]])


def weighted_sum(ns, weights):
    return sum([pair[0] * pair[1] for pair in zip(ns, weights)])


def alternating_caps(string):
    return ''.join(letter.upper() if i % 2 == 0 else letter.lower() for i, letter in enumerate(string))


def find_repeated_words(sentence):
    words = [word.lower() for word in re.findall('[a-zA-Z]+', sentence)]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}