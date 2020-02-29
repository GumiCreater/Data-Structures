from Queue import Queue


q = Queue()
q.enqueue("q")
q.enqueue("w")
q.enqueue("e")
print(q.isEmpty())
print(q.dequeue())
print(q.size())
q.dequeue()
q.dequeue()
print(q.isEmpty())