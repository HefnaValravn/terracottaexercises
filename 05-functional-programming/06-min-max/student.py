def closest(points, target_point):
    return min(points, key=lambda pair : calc_distance(pair, target_point))


def calc_distance(from_point, to_point):
    return ((to_point[0] - from_point[0])**2 + (to_point[1] - from_point[1])**2)**0.5