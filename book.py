class bookx:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        print('Self Pages=',self.pages)
        print("Other Pages=",other.pages)
        return self.pages+other.pages
class booky:
    def __init__(self,pages):
        self.pages=pages
        
b1=bookx(100)
b2=booky(150)
print("Total Pages=",b1+b2)     
   

