def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

#num = int(input("Enter a number: "))
for i in range(1,30):
    print("Factorial of",i, "is", factorial(i))
    
       