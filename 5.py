class Person():
    age = 0
    def __init__(self,initialAge):
        if(initialAge < 0):
            print("Age is not valid, setting to 0.")
        else:
            self.age = initialAge
	
	
    def yearPasses(self):
	    self.age += 1

    def amIOld(self):
        if(self.age > 0 and self.age < 13):
            print("You are young.")
        elif(self.age >= 13 and self.age <= 19):
            print("You are a teenager.")
        else:
            print("You are old.")    
p1 = Person(38)
p2 = Person(4)

p1.amIOld()
p2.yearPasses()