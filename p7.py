while True:
    print("\n--- Area Calculator ---")
    print("1. Circle")
    print("2. Triangle")
    print("3. Square")
    print("4. Rectangle")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        r = float(input("Enter radius: "))
        print("Area of Circle =", 3.14 * r * r)

    elif ch == 2:
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        print("Area of Triangle =", 0.5 * b * h)

    elif ch == 3:
        s = float(input("Enter side: "))
        print("Area of Square =", s * s)

    elif ch == 4:
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        print("Area of Rectangle =", l * w)

    elif ch == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")
