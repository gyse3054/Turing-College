from collections import Counter

X = int(input())
shoe_list = input().split()
new_shoe_list = []

for i in shoe_list:
    i = int(i)
    new_shoe_list.append(i)

N = int(input())
counter_dict = dict(Counter(new_shoe_list))
pisal = 0

for i in range(N):
    shoe_size, quantity = map(int, input().split())
    
    if shoe_size in counter_dict.keys():
        if counter_dict[shoe_size] != 0:
            counter_dict[shoe_size] -= 1
            pisal += quantity

print(pisal)