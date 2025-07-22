# Write a program to generate prime numbers with the help of a user defined
# function to test prime or not.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Enter The Range of No: "))

for i in range(2, n + 1):
    if is_prime(i):
        print(i)
