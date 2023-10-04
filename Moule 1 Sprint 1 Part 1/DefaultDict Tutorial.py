from collections import defaultdict
n,m = list(map(int,input().split()))

grpA = defaultdict(str)
# grpA directly stores the 1-based index positions as a string.
for i in range(1,n+1):
    grpA[input()] += f" {i}"

grpB = []
for i in range(m):
    grpB.append(input())

# lstrip is used to get rid of space present at beginning of the string due to "grpA[input()] += f" {i}"" .
for word in grpB:
    if word in grpA:
        print(str.lstrip(grpA[word]))
    else:
        print(-1)