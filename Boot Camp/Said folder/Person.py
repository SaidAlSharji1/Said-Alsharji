class Person:
    # constructr to creat Objects
    #initialize instance variables 
    def __init__(self, name, P_age ,salary): # we get defualt value of age 20
        self.name = name
        self.age = P_age
        self.salary = salary
    #use term of encapsulation
        #accesor methods
        
    def bounce(self):
       b = self.salary * 0.005
       return b 
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    #setter / mutour methods
    def set_name(self, newName):
        self.name = newName
    def set_age (self, newAge):
        self.age = newAge
    def run(self):
        print(self.name, "is running")
    def descrip(self):
        return f"Person name {self.name} is {self.age} years old"
    def laugh(self):
        print (f"{self.name} say hahahhaha")
    def say_hi(self):
        return f"hi you {self.name} as person"
        
    