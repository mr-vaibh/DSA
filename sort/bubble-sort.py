def bubble_sort(array):
    length = len(array)

    for i in range(length):
        for j in range(length):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
    
    return array


print(bubble_sort([5, 9, 2, 1, 67]))