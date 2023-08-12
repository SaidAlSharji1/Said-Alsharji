from QueueClass import Queue

def is_palindrome():
    q1=Queue()
    tb=""
    ta=""
    w=input("enter a word")
    z=len(w)
    for i in range(len(w)):
        q1.enqueue(w[i])
        tb+=w[i]
        ta+=w[z-1]
        print(w[z-1])
        z-=1
    if tb == ta:
        print("the word is palindrome ")
    else:
        print("the word is not palindrome ")

is_palindrome()