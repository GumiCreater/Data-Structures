from link import UnorderHead, Node, linklist


p = linklist()
p.add(1)
p.add(2)
p.add(4)
p.travel()
print("----------")
print(p.search(4))
print("----------")
p.add(3,3)
p.travel()
print("----------")
print(p.size())
print("----------")
p.remove(3)
p.travel()