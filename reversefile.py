#WAP TO STORE REVERSE OF ONE FILE TO ANOTHER FILE
# Write input to input.txt

f1 = open("input.txt", "w")
name = input("Enter Name: ")
f1.write(name)
f1.close()

# Read from input.txt
f1 = open("input.txt", "r")
data = f1.read()
f1.close()

# Write reversed content to output.txt
f2 = open("output.txt", "w")
f2.write(data[::-1])
f2.close()

# Read from output.txt and display
f3 = open("output.txt", "r")
str1 = f3.read()
f3.close()

print("The Content of File:-")
print(str1)
