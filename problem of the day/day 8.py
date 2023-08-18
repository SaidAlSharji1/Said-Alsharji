class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    def reverse_parts(self, k):
        if not self.head or k <= 0:
            return
        
        prev = None
        current = self.head
        count = 0
        
        while current and count < k:
            prev = current
            current = current.next
            count += 1
        
        if not current:
            return
        
        prev.next = None
        new_head = self.reverse(self.head)
        current_head = self.reverse(current)
        self.head = new_head
        
        # Find the last node of the reversed first part
        while new_head.next:
            new_head = new_head.next
        
        # Connect the last node of the reversed first part to the head of the remaining part
        new_head.next = current_head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

print("Original linked list:")
my_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Get user input for the value of K
k = int(input("Enter the value of K: "))

# Reverse the first part up to K and the rest
my_list.reverse_parts(k)

print("Linked list after reversing parts:")
my_list.display()