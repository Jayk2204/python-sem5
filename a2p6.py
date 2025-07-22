# Write a program to show variable length argument and its use.
def total_marks(*marks):
    total = sum(marks)
    print("Marks:", marks)
    print("Total Marks:", total)

total_marks(75, 80, 90)
total_marks(60, 70)
total_marks(88, 76, 92, 85, 69)
