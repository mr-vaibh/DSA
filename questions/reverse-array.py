arr = [3, 2, -1, 56, 10000, 167]

n = len(arr) - 1

for i in range(int((n + 1) / 2)):
    temp = arr[i]
    arr[i] = arr[n-i]
    arr[n-i] = temp

print(arr)
# O(N/2)
