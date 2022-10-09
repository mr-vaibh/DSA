# this merge sort do not return, rather it changes the existing array

def merge_two(left, right, array):
    p1 = p2 = k = 0

    # start a pointer and compare the arrays
    # in order to sort them
    while p1 < len(left) and p2 < len(right):
        if left[p1] < right[p2]:
            array[k] = left[p1]
            p1 += 1
        else:
            array[k] = right[p2]
            p2 += 1
        k += 1

    # iterating once more through both arrays
    # for just in case few elements are missed
    # due to different array length
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
        return

    midpoint = len(array) // 2 
    left_arr = array[:midpoint]
    right_arr = array[midpoint:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    merge_two(left_arr, right_arr, array)

# print(merge_two([2, 6], [4, 9, 10]))
x = [2, 4, 9, 5, 2]
merge_sort(x)
print(x)
