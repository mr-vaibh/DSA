def selection_sort(array):
    for i in range(len(array)-1):
        minimum_no_index = i
        for j in range(i+1, len(array)):            
            if array[j] < array[minimum_no_index]:
                minimum_no_index = j
        
        if i != minimum_no_index:
            array[i], array[minimum_no_index] = array[minimum_no_index], array[i]

x = [2, 4, 9, 5, 2]
selection_sort(x)
print(x)