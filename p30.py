def add_three(func):
    def wrapper(x):
        return func(x) + 3
    return wrapper

@add_three
def get_number(n):
    return n

num = int(input("Enter a number: "))
print("Result after adding 3:", get_number(num))
