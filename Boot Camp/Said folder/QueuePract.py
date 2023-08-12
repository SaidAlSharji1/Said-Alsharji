from QueueClass import Queue
lane = Queue()

lane.enqueue("A")
lane.enqueue("B")
lane.enqueue("C")
print(lane.peek())
print(lane.size())
print(f"the deleted valeue {lane.dequeue()}")
print(lane.peek())