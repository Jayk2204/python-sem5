# Q 17  method overloading to find sum of 2 or 3 numbers
class myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("a+b+c",a+b+c)
        elif a!=None and b!=None:
            print("a+b",a+b)
        else:
            print("Please Enter 2 or 3 Numbers")
m=myclass()
m.sum(3,4,5)
m.sum(5,5)
m.sum(10)