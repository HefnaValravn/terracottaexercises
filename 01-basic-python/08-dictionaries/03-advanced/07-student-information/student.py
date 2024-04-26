def process_data(string_data):
    result = {}
    for i in string_data:
        raw = i.split(",")
        dict = {'age':int(raw[1]), 'courses': raw[2:]}
        result[raw[0]] = dict
    
    return result


def average_age(data):
    total = 0
    count = 0

    for i in data.values():
        if 'age' in i: 
            total += i['age']
            count += 1
    if count == 0:
        return 0

    return total / count


def courses(data):
    final = set()

    for i in data.values():
        if 'courses' in i:
            final.update(i['courses'])
    
    return final


def most_common_courses(data):
    final = []

    for i in data.values():
        if 'courses' in i:
            final.extend(i['courses'])
    
    results = {}

    for i in final:
        results[i] = results.get(i, 0) + 1

    max_value = max(results.values())
    max_results = {key for key, value in results.items() if value == max_value}
    return max_results

