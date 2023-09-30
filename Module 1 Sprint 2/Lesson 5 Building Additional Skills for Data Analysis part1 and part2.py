
from collections import defaultdict #used for grouping and accumulating data
from pprint import pprint

d = defaultdict(list)

d['raymond'].append('red')
d['gytis'].append('blue')
d['aiste'].append('yellow')

d['raymond'].append('mac')
d['gytis'].append('pc')
d['aiste'].append('vtech')

pprint(d)

#after collecting data defaultdict is not needed

pprint(dict(d))

#Model one to many: dict(one, list_of_may)

a = {
    'one': ['uno'],
    'two': ['dos'],
    'three': ['tres'],
    'trio':['tres'],
    'free':['libre', 'gratis'],

}

pprint(a, width= 40)

s2e = defaultdict(list)
for eng, spanwords in a.items():
    for span in spanwords:
        s2e[span].append(eng)

pprint(s2e, width= 40)

lol = dict(one = 'uno', two ='dos', three = 'tres')
print({span: eng for eng, span in lol.items()})

import glob

glob.glob('*.txt') # Global wildcard expansion -> os.expand_wildcards()

#with open('data.csv', encoding = 'utf-8' ) as f:
#    print(f.read())

#To remove elements from iterator

it = iter('abcdefg')
print(next(it))
print(next(it))
print(list(it))


import csv
#with open('data.csv', encoding = 'utf-8' ) as f:    #SPLITS EACH ROW INTO A LIST
#    for row in csv.reader(f):
#               print(row)



t = ('Gytis', 'Sem', 54, 'gytiise@')
print(type(t))

fname, lname, age, email = t
print(email)




names  = 'gytis aiste tomas'.split()
colors = 'red blue tellow'.split()
cities = 'vilnius  vilnius kaunas la kaunas siauliai palanga klaipeda ny la'.split()

#Loop idioms

for name in names:
    print(name.upper())


#Numerate names option 1:
for i in range(len(names)):
    print(i+1, names[i].upper())

#Numerate names option 1:
for i, name in enumerate(names, start = 1):
    print(i,name)

#Reverse order:

for color in reversed(colors):
    print(color)

#Bring names together with colours in pairs 

for name, color in zip(names, colors):
    print(name, color)

#In alphapetical

for color in sorted(colors):
    print(color)


#By length
for color in sorted(colors, key = len):
    print(color)


#Without dublicates

for city in sorted(set(cities)):
    print(city)

# DISTINCT IS SET
# ORDER BY IS SORTED

for i, city in enumerate(reversed(sorted(set(cities)))):
    print(i, city)


for i, city in enumerate(map(str.upper, reversed(sorted(set(cities))))):
    print(i, city)


import collections
c = collections.Counter() #For counting things

c.most_common()

assert 5 + 3 ==8 #to check true or false it will give error
# assert 5 + 3 ==10 ERROR