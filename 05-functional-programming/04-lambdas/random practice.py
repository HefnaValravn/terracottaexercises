from functools import reduce


nums = [2, 4, 5, 6, 3, 11, 15]

filter_even = filter(lambda item: item % 2 != 0, nums)


print(list(filter_even))


reducing = reduce(lambda num1, num2: num1 * num2, nums)

print(reducing)


evening = lambda x : "Even" if x % 2 == 0 else "Odd"

print(evening(4))


doubling = [(lambda x: x*2)(x) for x in nums]


print(doubling)

students = [
    {'name': 'John', 'grade': 90},
    {'name': 'Jane', 'grade': 85},
    {'name': 'Dave', 'grade': 92}
]

sort_dict = sorted(students, key=lambda x: x['grade'], reverse=False)

max_dict = max(students, key=lambda x: x['grade'])

min_dict = min(students, key=lambda x: x['grade'])

print(sort_dict)

print(max_dict)

print(min_dict)



sum_list = reduce(lambda x, y: x + y, nums)


print(sum_list)

things = ["asdf", "fwoier", "fslierjwoei", "fsd", "wdoijwpwe", "s"]

five_char_or_more = list(filter(lambda x: len(x) >= 5, things))

print(five_char_or_more)

stuff = [[2, 3, 4], [2, 2], [6, 2, 3]]

sublist_sum = list(map(lambda sublist : sum(sublist), stuff))

print(sublist_sum)


create_dict = {x: (lambda x: x**2)(x) for x in range(1, 6)}

print(create_dict)


fizzbuzz = lambda x: "fizz" if x % 3 == 0 and x % 5 != 0 else "buzz" if x % 5 == 0 and x % 3 != 0 else "fizzbuzz" if x % 3 == 0 and x % 5 == 0 else x

print(fizzbuzz(15))

print(fizzbuzz(20))

print(fizzbuzz(7))


filter_and_square = [x**2 for x in nums if (lambda x: x % 2 == 0)(x)]
print(filter_and_square)

strings = ["this", "is", "a", "test"]

concat_list = reduce(lambda x, y: x + " " + y, strings)


print(concat_list)

lists = ["a", "f", ".", ",", "d", "w", "1", ";", "6"]

filter_and_upper = list(map(lambda x: x.upper(), filter(lambda x: x.isalpha(), lists)))

print(filter_and_upper)

data = [{'name': 'John', 'hobbies': ['reading', 'hiking']},
        {'name': 'Jane', 'hobbies': ['painting', 'swimming', 'running']},
        {'name': 'Dave', 'hobbies': ['gaming']}]

sort_data = sorted(data, key=lambda x: len(x['hobbies']))

print(sort_data)


nested_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [1, 1, 1]]

sublist_greater_10 = list(filter(lambda sublist : sum(sublist) > 10, nested_lists))


print(sublist_greater_10)

nums = [1, 2, 3, 5, 6, 7, 8]

product_of_filters = reduce(lambda x, y: x * y, filter(lambda x: x >= 5, nums))

print(product_of_filters)


strings = ["hello", "", "world", "", "python"]

#I originally thought the condition for the second part of this function was gonna be "not x", but filter() filters out anything that DOESN'T meet that requirement,
#so anything in the list that isn't null gets filtered out. that's why the condition for the second lambda function is just "x": anything that is null gets filtered
#out.
len_strings_non_empty = list(map(lambda x: len(x), filter(lambda x: x, strings)))

print(len_strings_non_empty)


nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

max_value = reduce(lambda x, y: x if x > y else y, nums)

print(max_value)

nums = [1, 2, 3, 4, 5]

odd_even_list = list(map(lambda x: "odd:" + str(x) if x % 2 != 0 else "even:" + str(x), nums))

print(odd_even_list)


nums = [-1, 2, -3, 4, -5, 6]


square_non_negative = [x**2 for x in nums if (lambda x: x > 0)(x)]

print(square_non_negative)

strings = ["apple", "banana", "orange", "grape", "kiwi"]

upper_non_a = list(map(lambda x: x.upper(), filter(lambda x: 'a' not in x, strings)))

print(upper_non_a)

strings = ["apple", "banana", "orange", "grape", "kiwi"]

sort_on_vowel = sorted(strings, key=lambda x: sum(1 for char in x if char in 'aeiou'))

print(sort_on_vowel)