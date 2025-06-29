# Write a program to swap two numbers without taking a temporary variable.
a=int(input("Enter No 1:-"))
b=int(input("Enter No 2:-"))
print("Before Swaping")
print("No 1:-",a)
print("No 2:-",b)
a=a+b
b=a-b
a=a-b
print("After Swaping")
print("No 1:-",a)
print("No 2:-",b)

