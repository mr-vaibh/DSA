def merge_two(left, right, array):
    p1 = p2 = k = 0

    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            array[k] = left[p1]
            p1 += 1
        else:
            array[k] = right[p2]
            p2 += 1
        k += 1
    while p1 < len(left):
        array[k] = left[p1]
        p1 += 1
        k += 1
    while p2 < len(right):
        array[k] = right[p2]
        p2 += 1
        k += 1

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        mid_point = len(array) // 2 
        left = array[:mid_point]
        right = array[mid_point:]

        merge_sort(left),
        merge_sort(right),
        
        merge_two(left, right, array)

# print(merge_two([2, 6], [4, 9, 10]))
x = [2, 4, 9, 5, 2]
merge_sort(x)
print(x)