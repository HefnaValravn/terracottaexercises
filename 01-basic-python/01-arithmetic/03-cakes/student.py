from math import floor
def cakes(eggs, butter, flour):
    return min(floor(eggs/5), floor(butter/250), floor(flour/250))