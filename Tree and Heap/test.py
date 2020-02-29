from BinaryHeap import BinHeap
from temp_creat import temp_creat


H = BinHeap()
H.buildHeap(temp_creat(5))
while H.listSize > 0:
    print(H.delMin(), " ")