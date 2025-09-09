#program 5
#Using Class method to hnalde COmmon features of all instances

class bird:
    wings=2 #static or class variable
    @classmethod
    def fly(cls,name):
        print('{} Flies With {}'.format(name,cls.wings))
        
bird.fly("Sparrow")
bird.fly("Het")    
    