""""
Write a python program that asks the user to enter a length in centimeters.
If the user enters a negative length, the program should tell the user that the
entry is invalid. Otherwise, the program should convert the length to inches
and print out the result. (2.54cm = 1 inch)."""
cm = float(input("Enter length in centimeters: "))

if cm < 0:
    print("Length cannot be negative.")
else:
    inches = cm / 2.54
    print("Length in inches:",inches)
