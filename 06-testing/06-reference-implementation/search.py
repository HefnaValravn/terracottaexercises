def linear_search(students, target_id):
    for student in students:
        if target_id == student.id:
            return student
    return None
        

def binary_search(students, target_id):
    left = 0
    right = len(students) - 1
    while left <= right:
        middle = (left + right) // 2
        if students[middle].id == target_id:
            return students[middle]
        elif students[middle].id < target_id:
            left = middle + 1
        elif students[middle].id > target_id:
            right = middle - 1
    
    return None