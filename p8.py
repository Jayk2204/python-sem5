cm = float(input("Enter length in centimeters: "))

if cm < 0:
    print("Invalid entry. Length cannot be negative.")
else:
    inches = cm / 2.54
    print("Length in inches:", inches)
