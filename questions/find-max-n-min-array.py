arr = [3, 2, -1, 56, 10000, 167]

maximum, minimum = arr[0], arr[0]

for x in arr:
    if x < minimum:
        minimum = x
    if x > maximum:
        maximum = x

print(maximum, minimum)
# O(N)
