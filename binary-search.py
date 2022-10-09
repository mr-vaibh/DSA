numbers = [18, 29, 38, 55, 56, 59, 66, 69, 78, 92]

def binary_search(array, number):
    left_index = 0
    right_index = len(array) - 1

    mid_index = (left_index + right_index) // 2
    
    while left_index <= right_index:
        mid_number = array[mid_index]
        
        if mid_number == number:
            return mid_index
        elif mid_number < number:
            left_index = mid_index + 1
        elif mid_number > number:
            right_index = mid_index - 1

        mid_index = (left_index + right_index) // 2
    
    return -1

def binary_search_recursive(array, number, left_index=None, right_index=None):
    left_index = left_index or 0
    right_index = right_index or len(array) - 1
    
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2
    mid_number = array[mid_index]

    if mid_number == number:
        return mid_index
    elif mid_number < number:
        left_index = mid_index + 1
    elif mid_number > number:
        right_index = mid_index - 1

    return binary_search_recursive(array, number, left_index=left_index, right_index=right_index)
    

print(binary_search(numbers, 38))
print(binary_search_recursive(numbers, 38))
