from StackClass import Stack

def letter():
    n=int(input("enter the number of the letters"))
    s1= Stack()
    for i in range(n):
        x=input("Enter any letters")
        s1.push(x)
    for l in range (n):
        print(s1.pop())
    
letter()
    
    
    
    