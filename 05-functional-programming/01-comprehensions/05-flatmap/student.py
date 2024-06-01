from util import Card

def genres(movies):
    return set(genre for movie in movies for genre in movie.genres)


def actors(movies):
    return set(actor for movie in movies for actor in movie.actors)


def repeat_consecutive(xs, n):
    return [item for item in xs for _ in range(n)]


def repeat_alternating(xs, n):
    return [item for _ in range(n) for item in xs]


def cards(values, suits):
    return {Card(value, suit) for value in values for suit in suits}