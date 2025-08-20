lst = [10, 20, 30, 20, 40, 50, 20]
x = int(input("Enter element to search: "))

count = 0
for i in lst:
    if i == x:
        count += 1

if count > 0:
    print(x, "found", count, "time(s) in the list")
else:
    print(x, "not found in the list")
5