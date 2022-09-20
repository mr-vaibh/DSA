arr = [1,2,3]

p1 = 0

for i in range(1, len(arr)):
    if arr[p1] < arr[i]:
        p1 = i

print(p1)
# O(N)
