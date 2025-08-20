name = input("Enter student name: ")
roll = input("Enter roll number: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("\n----- Marksheet -----")
print("Name:", name)
print("Roll No:", roll)
print("Subject 1:", m1)
print("Subject 2:", m2)
print("Subject 3:", m3)
print("Total Marks:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A+")
elif average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
