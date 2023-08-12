#add comments LIFO
#Think how to add/apply is_FULL??
class Stack:
    def __init__(self):
        self.items = []
        

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty, cannot pop an item.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty, cannot peek an item.")

    def size(self):
        return len(self.items)
    
    