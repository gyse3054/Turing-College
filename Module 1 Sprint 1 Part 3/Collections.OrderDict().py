from collections import OrderedDict

N = int(input())

ordered_dic = OrderedDict()

for i in range(N):
    elements = input().split()
    fruit = " ".join(elements[:-1])
    price = int(elements[-1])
    if fruit in ordered_dic:
        ordered_dic[fruit] += price
    else:
        ordered_dic[fruit] = price
    
for i in ordered_dic:
    print(i, ordered_dic[i])