from math import fsum
from collections import defaultdict

#fsum gives exact value. Used for precise summing
#defauldict can be used for grouping.
#defaultdict creates a new container to create to store elements with common feature

d = defaultdict(set)
d['t'].add('tom')
d['m'].add('marry')
d['t'].add('tim')
d['t'].add('tom')
d['m'].add('martin')

print(d)

from pprint import pprint

pprint(d, width = 40)
d = defaultdict(list)

#for name in names:
##    feature = name[-1]
 #   d[feature].append(name)


#KEY FUNCTIONS. For sorting, mnimum, maximum, grouping. 
#Key takes one argument and transforms it to a key

names = defaultdict(list)
names = '''Gytis Sarunas, Arunas, Aiste'''.split()

pprint(sorted(names, key = len))

#ZIP

print(list(zip('abcdef', 'ghijklm'))) # pairs all items execpt m as the  count of letters are not identical.

from itertools import zip_longest

print(list(zip_longest('abcdef', 'ghijklm'))) #to solve above problem
print(list(zip_longest('abcdef', 'ghijklm', fillvalue= 'lol'))) #to solve above


m = [
    [10,20],
    [30,50],
    [50,60],
]
# 3 rows by 2 column

pprint(list(zip(*m)), width = 15)

for row in m:
    print(row)

it = iter('abcd')
print(it)
print(list(it))

#fsum() is used for more accurate results
#defaultdict is used for grouping
#min, max, sorted, nsmallest, merge
#zip(*data) to transpose 2D data
#nested list to flatten list
# to create iterator as a list just list(iterator)

