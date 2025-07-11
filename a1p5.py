""" Create student marksheet. (Enter Rollno, name and three subjects marks.
 Find Total, Average and Grade from them.)"""
 
rollno = input("Enter Roll Number: ")
name = input("Enter Student Name: ")

math = float(input("Enter marks for math:   "))
eng = float(input("Enter marks for eng: "))
sci = float(input("Enter marks for sci: "))


total = math + eng + sci
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F (Fail)"


print("\n------ Student Marksheet ------")
print("Roll Number :", rollno)
print("Name        :", name)
print("Subject 1   :", math)
print("Subject 2   :", eng)
print("Subject 3   :", sci)
print("Total Marks :", total)
print("Average     :", (average, 2))
print("Grade       :", grade)
