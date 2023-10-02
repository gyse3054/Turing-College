
from collections import deque
import random




def funkcija(deq):
    dek = deque()
    
    for i in range(1):
        dek.append(1)
        dek.append(2)
        dek.append(3)
        dek.appendleft(4)
        dek.pop()
        dek.popleft()

    a = " ".join(map(str,dek))
    print(a)



d = deque()
funkcija(d)

