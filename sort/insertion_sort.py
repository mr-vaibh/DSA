def insertion_sort(array):
    for i in range(1, len(array)):
        pointer = array[i]

        left = i - 1
        while array[left] >= pointer and left >= 0:
            array[left+1] = array[left]
            left -= 1
        array[left+1] = pointer

    return array

print(insertion_sort([2, 4, 10, 9, 5, 2]))