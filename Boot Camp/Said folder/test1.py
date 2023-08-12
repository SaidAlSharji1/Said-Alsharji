from Person import Person
from TeacherClass import Teacher 
def main():
    p1= Person("ahmed", 24 ,1500)
    t1= Teacher("hmoad",20,1500,2001)
    print(p1.descrip())
    print(p1.bounce())
    print(t1.descrip())
    print(t1.bounce())
    
main()