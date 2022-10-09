def binary_search(arr, num):
    left_p = 0
    right_p = len(arr) - 1

    while left_p <= right_p:
        mid_p = (left_p + right_p) // 2

        if arr[mid_p] == num:
            return mid_p
        elif arr[mid_p] < num:
            left_p = mid_p + 1
        elif arr[mid_p] > num:
            right_p = mid_p - 1

    return -1

def binary_search_recursive(arr, num, left_p = None, right_p = None):
    left_p = left_p or 0
    right_p = right_p or len(arr) - 1

    if left_p > right_p:
        return -1

    mid_p = (left_p + right_p) // 2

    if arr[mid_p] == num:
        return mid_p
    elif arr[mid_p] < num:
        left_p = mid_p + 1
    elif arr[mid_p] > num:
        right_p = mid_p - 1

    return binary_search_recursive(arr, num, left_p=left_p, right_p=right_p)

x = [1,2,3,6,9,46]
ans1 = binary_search(x, 9)
ans2 = binary_search_recursive(x, 9)
print(ans1)
print(ans2)
