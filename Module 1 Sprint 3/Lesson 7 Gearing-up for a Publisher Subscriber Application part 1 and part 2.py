

print('The answer is \u0664\u0662 today')
s = 'L' + chr(246) + 'wis'
t = 'L' + chr(111) + chr(776) + 'wis'

print(s) 
print(t)
print(t == s)

import unicodedata

u = unicodedata.normalize('NFC', t) #to match look ups

#named tuple
import collections
Person = collections.namedtuple('Person', ['fname', 'lname', 'age', 'email'])
p = Person('Gytis', 'Semenas', 27, 'gytisse')


#sorted data and bisect (searching inside ranges)
import bisect
cuts = [60,70,80,90]
grades = 'FDCBA'

print(grades[bisect.bisect(cuts, 76)])

print([grades[bisect.bisect(cuts, score)] for score in [76,92,80,70,45]])

print(sorted([10,5,20] + [1,11,25]))

a = [1,11,25]
b = [5,10,20]
c = [2,15,21]

from heapq import merge

print(list(merge(a,b,c)))

it = merge(a,b,c)
print(next(it))
print(next(it))

from itertools import islice

print(list(islice('abcdefhgi', 3)))
print(list(islice('abcdefhgi', None, 3)))
print(list(islice('abcdefhgi',2,4)))
print(list(islice('abcdefhgi', 0,2,4)))


s = 'he'
t = 'llo'
u = 'hello'
v = s + t

print(u ==v)
print(id(u))
print(id(v))

import sys #TO NOT HAVE THE SAME USER NAME 
sys.intern('hello')

import random

random.uniform(1000,11100)
random.expovariate(1/ 5) #used for arrival times simulation


import time

#time.sleep(5); print('Done') #lag
print(time.time())
print(time.ctime())


import hashlib

print(hashlib.sha512('The tale of two cities'.encode('utf-8')))
b = 'The tale of two cities'.encode('utf-8')
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
print(b)


p = 'The tale of two cities'.encode('utf-8')
h = hashlib.pbkdf2_hmac('sha256', p, b'some phrase', 100000)

s = 'the quick'
t = 'brown fox'
print(s + t)


los = ['gytis', 'nemegsta', 'pythono']
print(los)
print(' '.join(los))

#Ternary operator == conditional expression

score = 70
print('pass' if score >= 70 else 'fail')

print(bool('hello')) #true
print(bool('')) #false


def f(x, s = None):
    s = s or 'default'
    print(x,s)

f(10, 'some value')
f(10)