#WAP TO READ TWO FILE FILE1 AND FILE2. NOW STORE THE CONTENT OF BOTH THE FILE TO FILE 3.
#WAP TO STORE REVERSE OF ONE FILE TO ANOTHER FILE
# Write input to input.txt

f1 = open("f1.txt", "w")
name = input("Enter Name: ")
f1.write(name)
f1.close()

f2 = open("f2.txt", "w")
fname = input("Enter Father Name: ")
f2.write(fname)
f2.close()

f1=open("f1.txt","r")
str1=f1.read()
f1.close()


f2=open("f2.txt","r")
str2=f2.read()
f2.close()

f3=open("f3.txt","w")
f3.write(str1)
f3.write(str2)
f3.close()



