try:
    a=input("Enter a Number:-") 
    b=input("Enter Second Number:-")
    c=int(a)/int(b)
    print(c)
except ZeroDivisionError:
    print("Divide by Zero error is Raised")
except ValueError:
    print("Value error is Raised")
except TypeError:
    print("Type error is Raised")
except NameError:
    print("Name error is Raised")
else:
    print("There is No Errror")
finally:
    print("Have a Nice Day")