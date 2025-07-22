# Write a program to demonstrate the use of Positional argument, keyword
# argument and default arguments.
def employee_info(name, age, department="DATA SCIENCE"):
    print("Name:", name)
    print("Age:", age)
    print("Department:", department)

# Positional arguments
employee_info("Jaykishan", 19)

# Keyword arguments
employee_info(name="Niluu", age=19, department="Cyber Security")

# Default argument used (department)
employee_info(name="Mihir", age=20)

