def merge_two(arr1, arr2):
    sorted_arr = []
    p1 = p2 = 0

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            sorted_arr.append(arr1[p1])
            p1 += 1
        else:
            sorted_arr.append(arr2[p2])
            p2 += 1
    
    while p1 < len(arr1):
        sorted_arr.append(arr1[p1])
        p1 += 1
    while p2 < len(arr2):
        sorted_arr.append(arr2[p2])
        p2 += 1

    return sorted_arr

def merge_sort(array):
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2
    left_arr = array[:midpoint]
    right_arr = array[midpoint:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    sorted_arr = merge_two(left_arr, right_arr)

    return sorted_arr

x = [2,4,35,8,68,5,24,9]
new_arr = merge_sort(x)
print(new_arr)
