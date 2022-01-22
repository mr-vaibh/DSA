def shell_sort(array):
    gap = len(array) // 2

    while gap > 0:
        for i in range(gap, len(array)):
            pointer = array[i]

            while i >= 0 and array[i-gap] > pointer:
                array[i] = array[i-gap]
                i -= gap
            array[i] = pointer
        
        gap //= 2

x = [2, 3, 9, 5, 3]
shell_sort(x)
print(x)