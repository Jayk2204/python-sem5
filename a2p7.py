# 7. Write a lambda/Anonymous function to find bigger number in two given numbers.
bigger = lambda a, b: a if a > b else b

# Example usage
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Bigger number is:", bigger(x, y))
