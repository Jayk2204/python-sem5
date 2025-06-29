"""
Write a menu driven python program which perform the following:
Find area of circle
Find area of triangle
Find area of square
Find area of rectangle
Find Simple interest.
"""
def area_of_circle():
    r = float(input("Enter R of the circle: "))
    area = 3.14* r * r
    print("Area of Circle =",area)

def area_of_triangle():
    b = float(input("Enter B of the triangle: "))
    h = float(input("Enter H of the triangle: "))
    area = 0.5 * b * h
    print("Area of Triangle =",area)

def area_of_square():
    side = float(input("Enter side of the square: "))
    area = side * side
    print("Area of Square =",area)

def area_of_rectangle():
    l = float(input("Enter L of the rectangle: "))
    w = float(input("Enter W of the rectangle: "))
    area = l * w
    print("Area of Rectangle =",area)

def simple_interest():
    p = float(input("Enter P amount: "))
    r = float(input("Enter R "))
    t = float(input("Enter T: "))
    si = (p * r * t) / 100
    print("Simple Interest =",si)

while True:
    print("\n--- Menu ---")
    print("1. Area of Circle")
    print("2. Area of Triangle")
    print("3. Area of Square")
    print("4. Area of Rectangle")
    print("5. Simple Interest")
    print("6. Exit")

    choice = input("Enter No (1-6): ")

    if choice == '1':
        area_of_circle()
    elif choice == '2':
        area_of_triangle()
    elif choice == '3':
        area_of_square()
    elif choice == '4':
        area_of_rectangle()
    elif choice == '5':
        simple_interest()
    elif choice == '6':
        print("Bye!")
        break
    else:
        print("Please enter a number between 1 and 6.")

