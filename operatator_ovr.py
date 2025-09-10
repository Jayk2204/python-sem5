class point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,other):
        x=self.x+other.x
        y=self.y+other.y
        return point(x,y)
p1=point(1,2)
p2=point(0,3)
p3=p1+p2
print("P3x=",p3.x,'P3y=',p3.y)