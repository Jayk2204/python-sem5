n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

for i in range(n):
    for j in range(n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted array:", arr)
