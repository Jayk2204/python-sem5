#Create static method thAT COUNT no of Innstances Created

class trial:
    count=0
    def __init__(self):
        trial.count+=1
    @staticmethod
    def countList():
        print("Count",trial.count)
        
t1=trial()
t2=trial()
t3=trial()
t=trial()

trial.countList()