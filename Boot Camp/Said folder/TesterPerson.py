from Person import Person
from StudentClass import Student
from TeacherClass import Teacher# from file name import class name 
def main():
    Said = Person("Said Al-Sharji", 25)
    person2 = Person("Ali", 12)
    print(Said.say_hi())
    print(person2.say_hi())
    std1 = Student("Omar" , 8 , 2023)
    std2 = Student("Ahmed" , 21 , 2020)
    std2.run()
    print (Said.get_name())
    Said.set_name("Said Sultan Al-Sharji")
    print (Said.get_name())
    print(Said.descrip()) # it's retutn so we should print it 
    Said.run() #it print in class so we should not print it 
    print(person2.descrip())
    Said.laugh()
    person2.laugh()
    print(std1.say_hi())
    print(Student.say_hi(std2))
    print(std2.descrip()) # it used person method
    t1 = Teacher("Mohamed", 45, 1500)
    print(t1.say_hi())
    
    


main()